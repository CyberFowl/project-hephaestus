import os
import time
import assets
import pyautogui as pagui

print("Hephaestus Search\nType 'p:' to enter private mode")
print("Query: ", end="")
reply = input().lower()
if reply != "p:":
    search = reply.split(" ")[0:]
    search = " ".join(search)

    os.startfile(assets.file_dict["dev"])
    time.sleep(2)
    pagui.hotkey("win", "up")

    pagui.hotkey("ctrl", "l")
    pagui.write(search, interval=0.001)
    pagui.press("enter")
else:
    print("Query [Private]: ", end="")
    reply = input().lower()
    search = reply.split(" ")[0:]
    search = " ".join(search)

    os.startfile(assets.file_dict["dev"])
    time.sleep(2)
    pagui.hotkey("win", "up")

    pagui.hotkey("ctrl", "shift", "p")

    pagui.hotkey("ctrl", "l")
    pagui.write(search, interval=0.001)
    pagui.press("enter")

    time.sleep(1)

    pagui.hotkey("alt", "tab")
    pagui.hotkey("ctrl", "w")