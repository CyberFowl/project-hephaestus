import os
import time
import assets
import pyautogui as pagui

pagui.hotkey("win", "up")

print("Query: ", end="")
reply = input().lower()
search = reply.split(" ")[0:]
search = " ".join(search)

os.startfile(assets.file_dict["dev"])
time.sleep(2)
pagui.hotkey("win", "up")

pagui.hotkey("ctrl", "l")
pagui.write(search, interval=0.001)
pagui.press("enter")