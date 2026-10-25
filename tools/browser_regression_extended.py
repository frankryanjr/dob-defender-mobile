#!/usr/bin/env python3
"""SHA-guarded deterministic Chromium regression checks. Synthetic targets; mocked API."""
import argparse, hashlib, json
from pathlib import Path
from playwright.sync_api import sync_playwright

parser = argparse.ArgumentParser()
parser.add_argument("html", type=Path)
parser.add_argument("--sha", required=True)
parser.add_argument("--chromium", default="/usr/bin/chromium")
args = parser.parse_args()
raw = args.html.read_bytes()
actual = hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
if actual != args.sha:
    raise ValueError("Production SHA mismatch: " + actual)
html = raw.decode("utf-8")
start = html.index("function hit(e,b)")
end = html.index("})();\n</script>", start)
hook = """
window.__ddRegression={
hit:(type,hp=1)=>{const e={type,x:60,y:110,vx:0,vy:0,hp,r:9,mandatory:false};const b={t:1};const before=score;hit(e,b);return {delta:score-before,hp:e.hp,bullet:b.t}},
swept:()=>{const before=score;const e={type:"meteor",x:175,y:175,vx:0,vy:0,hp:1,r:10,mandatory:false,phase:0};const b={x:165,y:175,px:165,py:175,vx:1300,vy:0,t:1};enemies.push(e);shots.push(b);updateNight(.016);return {delta:score-before,hp:e.hp,bullet:b.t}},
impact:()=>{const before=shield;const e={type:"meteor",x:W/2,y:floor()-100,hp:1,r:8,mandatory:true};pendingMandatory++;impact(e,false);return {damage:before-shield,hp:e.hp}}
};
"""
instrumented = html[:end]+hook+html[end:]
errors = []
with sync_playwright() as pw:
    browser = pw.chromium.launch(executable_path=args.chromium, headless=True, args=["--no-sandbox","--disable-dev-shm-usage"])
    try:
        page = browser.new_page(viewport={"width":390,"height":844}, is_mobile=True, has_touch=True)
        page.on("pageerror",lambda e:errors.append(str(e)))
        def reply(route):
            payload={"player":{"player_id":"regression-fixture","nickname":"Tester","best_score":0,"best_night":1}} if route.request.method=="POST" else {"scores":[]}
            route.fulfill(status=200,content_type="application/json",body=json.dumps(payload))
        page.route("**/functions/v1/dob-leaderboard",reply)
        page.set_content(instrumented,wait_until="commit",timeout=40000)
        page.locator("#ddApprovedStartButtonV1").click()
        assert page.locator("#ddCallsignGate").is_visible()
        page.locator("#ddCallsignDefend").click()
        page.wait_for_function("document.querySelector('#ddCallsignGate').hidden",timeout=10000)
        page.wait_for_timeout(6500)
        result = page.evaluate("() => ['meteor','comet','sat','asteroid'].map(t=>window.__ddRegression.hit(t))")
        assert [x["delta"] for x in result]==[10,5,5,10], result
        assert all(x["hp"]==0 and x["bullet"]==0 for x in result), result
        armored = page.evaluate("() => [window.__ddRegression.hit('asteroid',3),window.__ddRegression.hit('asteroid',2)]")
        assert [(x["delta"],x["hp"]) for x in armored]==[(5,2),(5,1)], armored
        swept = page.evaluate("() => window.__ddRegression.swept()")
        assert swept=={"delta":10,"hp":0,"bullet":0}, swept
        impact = page.evaluate("() => window.__ddRegression.impact()")
        assert impact=={"damage":20,"hp":0}, impact
        assets = page.evaluate("""() => {const c=document.querySelector('canvas');const d=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let pixels=0;for(let i=3;i<d.length;i+=4)if(d[i])pixels++;const imgs=[...document.images];const m=document.querySelector('#ddGameplayMusic');return {pixels,images:imgs.length,decoded:imgs.filter(x=>x.naturalWidth>0&&x.naturalHeight>0).length,musicVolume:m.volume,musicLoop:m.loop,musicReady:m.readyState}}""")
        assert assets["pixels"]>0 and assets["images"]>0 and assets["decoded"]==assets["images"], assets
        assert assets["musicVolume"]==0.2 and assets["musicLoop"] is True, assets
        assert not errors,errors
        print(json.dumps({"result":"PASS","sha":actual,"scoring":result,"armored":armored,"swept":swept,"impact":impact,"assets":assets,"page_errors":0,"note":"synthetic collision input; mocked leaderboard; actual music playback unverified"}))
    finally:
        browser.close()
