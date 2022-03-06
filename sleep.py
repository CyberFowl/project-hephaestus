import time
import pyautogui as pagui

pagui.hotkey("win", "up")
while True:
    pagui.click()
    pagui.press("esc")
    time.sleep(2700)
    print("Click")