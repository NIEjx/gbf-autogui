import pyautogui
import pygetwindow as gw
import time
import random
from PIL import Image, ImageDraw
import os

import tkinter as tk
from threading import Thread
running = False

def getChromeWindow(title):
    windows = gw.getWindowsWithTitle(title)
    if not windows:
        print(f"not find window {title}")
        windows = [w for w in gw.getWindowsWithTitle("Chrome") if w.isActive]
    return windows[0] if windows else None


def clickCenter(window):
    x = window.left + window.width/2+random.randint(-10, 10)
    y = window.top + window.height/2+random.randint(-10, 10)
    pyautogui.click(x, y)

def clickInWindow(index, window, buttonImagePath, timeout=10, confidence=0.85, debug=False):
    print(f'attempt to click {buttonImagePath}')
    region = (window.left, window.top, window.width, window.height)
    screenshot = pyautogui.screenshot(region=region)

    startTime = time.time()
    while time.time() - startTime < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(buttonImagePath, region=region, confidence=confidence)
            if location:
                # human like
                x = location.x + random.randint(-3, 3)
                y = location.y + random.randint(-3, 3)
                pyautogui.click(x, y)
                print(f'click {buttonImagePath}')
                if debug:
                    print(f'click {x}, {y}')
                    draw = ImageDraw.Draw(screenshot)
                    local_x = x  - window.left
                    local_y = y - window.top
                    r = 8
                    draw.ellipse((local_x - r, local_y - r, local_x + r, local_y + r), outline="red", width=3)
                    fileName = f'screenshot\\{index}_click.png'
                    if not os.path.isdir("screenshot"):
                        os.mkdir("screenshot")
                    screenshot.save(fileName)
                return True
        except:
            pass
        time.sleep(0.5)
    print(f'{buttonImagePath} not found')
    return False

def findInWindow(index, window, buttonImagePath, timeout=10, confidence=0.85, debug=False):
    print(f'attempt to click {buttonImagePath}')
    region = (window.left, window.top, window.width, window.height)
    screenshot = pyautogui.screenshot(region=region)

    startTime = time.time()
    while time.time() - startTime < timeout:
        try:
            location = pyautogui.locateCenterOnScreen(buttonImagePath, region=region, confidence=confidence)
            if location:
                # human like
                x = location.x + random.randint(-3, 3)
                y = location.y + random.randint(-3, 3)
                pyautogui.click(x, y)
                print(f'click {buttonImagePath}')
                if debug:
                    print(f'click {x}, {y}')
                    draw = ImageDraw.Draw(screenshot)
                    local_x = x  - window.left
                    local_y = y - window.top
                    r = 8
                    draw.ellipse((local_x - r, local_y - r, local_x + r, local_y + r), outline="red", width=3)
                    fileName = f'screenshot\\{index}_click.png'
                    if not os.path.isdir("screenshot"):
                        os.mkdir("screenshot")
                    screenshot.save(fileName)
                return True
        except:
            pass
        time.sleep(0.5)
        pyautogui.moveTo(window.left+window.width/2, window.top+window.height/2)

        pyautogui.scroll(-500)
    print(f'{buttonImagePath} not found')
    return False

def ifButtonInWindow(window, buttonImagePath, confidence=0.85):
    region = (window.left, window.top, window.width, window.height)
    try:
        location = pyautogui.locateCenterOnScreen(buttonImagePath, region=region, confidence=confidence)
        if location:
            return True
    except:
        pass
    return False
    
def raidCollectMeat(window):
    print("肉集め")
    stepCtn = 1
    if not findInWindow(stepCtn, window, "gbf\\ss_light_zeus_250.png"):     
        if not findInWindow(stepCtn, window, "gbf\\ss_light_lucifer.png"):
            print("not found friend summon")
            return
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\ok.png")
    stepCtn+=1
    time.sleep(3)
    clickInWindow(stepCtn, window, "gbf\\battle_gran.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\skill_reriba_augment.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\skill_reriba_limit.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\battle_back.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\battle_summon.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\battle_ss_light_zeus_250.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\ok.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\battle_back.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\battle_attack.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\battle_auto.png", timeout=20)
    stepCtn+=1
    while not ifButtonInWindow(window, "gbf\\ok.png", confidence=0.9):
        print("waiting for battle end")
        time.sleep(20)

    while not ifButtonInWindow(window, "gbf\\replay_battle.png"):
        clickInWindow(stepCtn, window, "gbf\\ok.png")
        stepCtn+=1
        time.sleep(0.1)
        clickCenter(window)
        time.sleep(0.1)
    
    clickInWindow(stepCtn, window, "gbf\\replay_battle.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\ok.png", timeout=1)
    
def raidHell(window):
    stepCtn = 1
    if not findInWindow(stepCtn, window, "gbf\\ss_light_lucifer.png"):     
        if not findInWindow(stepCtn, window, "gbf\\ss_light_zeus_250.png"):
            print("not found friend summon")
            return   
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\ok.png")
    stepCtn+=1
    time.sleep(5)
    clickInWindow(stepCtn, window, "gbf\\battle_summon.png")
    stepCtn+=1
    # コンテンツ切り替え
    time.sleep(0.5)
    clickInWindow(stepCtn, window, "gbf\\battle_ss_light_lucifer.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\ok.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\battle_fullauto.png")
    stepCtn+=1
    while not ifButtonInWindow(window, "gbf\\ok.png"):
        print("waiting for battle end")
        time.sleep(10)
        if clickInWindow(stepCtn, window, "gbf\\battle_summon.png", timeout=2):
            stepCtn+=1
            # コンテンツ切り替え
            time.sleep(0.5)
            if clickInWindow(stepCtn, window, "gbf\\battle_ss_light_lucifer.png", timeout=2):
                stepCtn+=1
                clickInWindow(stepCtn, window, "gbf\\ok.png", timeout=2)
                stepCtn+=1
            elif  clickInWindow(stepCtn, window, "gbf\\battle_ss_light_zeus.png", timeout=2):
                stepCtn+=1
                clickInWindow(stepCtn, window, "gbf\\ok.png", timeout=2)
                stepCtn+=1

    while not ifButtonInWindow(window, "gbf\\replay_battle.png"):
        clickInWindow(stepCtn, window, "gbf\\ok.png")
        stepCtn+=1
        time.sleep(0.1)
        clickCenter(window)
        time.sleep(0.1)

    clickInWindow(stepCtn, window, "gbf\\replay_battle.png")
    stepCtn+=1
    clickInWindow(stepCtn, window, "gbf\\ok.png", timeout=2)
    
def runBattle(func):
    print("finding GBF window")
    window = getChromeWindow("グランブルーファンタジー")
    if not window:
        print("GBF window not found")
        return
    if window.left < 0 or window.top < 0:
        print(f"Please replace the window, current left:{window.left}, top:{window.top}")
        return
    func(window)

def playerUI():
    window = tk.Tk()
    window.title("AutoScript")
    window.geometry("300x150")
    def startHell():
        global running
        running = True
        def run():
            while running:
                print("run hell auto battle")
                stop_btn.pack()
                start_hell_btn.pack_forget()
                start_Meet_btn.pack_forget()
                runBattle(raidHell)
                time.sleep(3)
        Thread(target=run, daemon=True).start()

    def startMeat():
        global running
        running = True
        def run():
            while running:
                print("run meat auto battle")
                stop_btn.pack()
                start_hell_btn.pack_forget()
                start_Meet_btn.pack_forget()
                runBattle(raidCollectMeat)
                time.sleep(3)
        Thread(target=run, daemon=True).start()

    def stopScript():
        global running
        running = False
        start_hell_btn.pack()
        start_Meet_btn.pack()
        stop_btn.pack_forget()
        print("stop")

    start_hell_btn = tk.Button(window, text="Hell auto", command=startHell)
    start_hell_btn.pack(pady=10)
    start_Meet_btn = tk.Button(window, text="Meat auto", command=startMeat)
    start_Meet_btn.pack(pady=10)

    stop_btn = tk.Button(window, text="Stop", command=stopScript)
    stop_btn.pack(pady=10)
    stop_btn.pack_forget()
    window.mainloop()

playerUI()



