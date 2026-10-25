#!/usr/bin/env python3
"""Chromium/Playwright smoke checks on SHA-verified production. Mocked backend only."""
import argparse, hashlib, json
from pathlib import Path
from playwright.sync_api import sync_playwright

p=argparse.ArgumentParser()
p.add_argument("html",type=Path)
p.add_argument("--sha",required=True)
p.add_argument("--chromium",default="/usr/bin/chromium")
a=p.parse_args()
data=a.html.read_bytes()
sha=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
assert sha==a.sha,"Production SHA mismatch"
errors=[]; calls=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path=a.chromium,headless=True,args=["--no-sandbox","--disable-dev-shm-usage"])
    page=browser.new_page(viewport={"width":390,"height":844},is_mobile=True,has_touch=True)
    page.on("pageerror",lambda e:errors.append(str(e)))
    def fake_api(route):
        r=route.request
        payload=r.post_data_json if r.method=="POST" else {}
        calls.append(payload.get("action","GET"))
        player={"player_id":"test-fixture","nickname":payload.get("nickname","TestPilot"),"best_score":0,"best_night":1}
        route.fulfill(status=200,content_type="application/json",body=json.dumps({"player":player} if r.method=="POST" else {"scores":[]}))
    page.route("**/functions/v1/dob-leaderboard",fake_api)
    page.set_content(data.decode("utf-8"),wait_until="commit",timeout=40000)
    page.locator("#ddApprovedStartButtonV1").click(timeout=10000)
    assert page.locator("#ddCallsignGate").is_visible()
    page.locator("#ddCallsignDefend").click(timeout=10000)
    page.wait_for_function("document.querySelector('#ddCallsignGate').hidden",timeout=10000)
    assert "register" in calls
    page.wait_for_timeout(6500)  # Natural opening countdown
    before=page.locator("#knob").evaluate("(e)=>e.style.left")
    rect=page.locator("#track").bounding_box()
    x=rect["x"]+rect["width"]/2; y=rect["y"]+rect["height"]/2
    page.mouse.move(x,y);page.mouse.down();page.mouse.move(x+55,y,steps=6);page.mouse.up()
    after=page.locator("#knob").evaluate("(e)=>e.style.left")
    assert before!=after,"Aim did not change"
    energy_before=page.locator("#energyVal").inner_text()
    page.mouse.click(190,350)
    page.wait_for_timeout(150)
    energy_after=page.locator("#energyVal").inner_text()
    assert energy_after!=energy_before,"Shot did not consume energy"
    page.locator("#pauseBtn").click()
    assert page.locator("#pauseBtn").get_attribute("aria-label")=="Resume game"
    paused=page.locator("#energyVal").inner_text()
    page.mouse.click(190,350);page.wait_for_timeout(100)
    assert page.locator("#energyVal").inner_text()==paused,"Shot occurred while paused"
    page.locator("#pauseBtn").click()
    assert page.locator("#pauseBtn").get_attribute("aria-label")=="Pause game"
    assert not errors,errors
    print(json.dumps({"result":"PASS","sha":sha,"gate":True,"mock_registration":True,"aim":[before,after],"laser":[energy_before,energy_after],"pause":True,"page_errors":0}))
    browser.close()
