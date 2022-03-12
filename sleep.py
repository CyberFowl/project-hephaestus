import os
import time
import pyautogui as pagui

os.system("color 4")
pagui.hotkey("win", "up")
while True:
    pagui.click()
    pagui.press("esc")
    time.sleep(2700)
    print("Click")