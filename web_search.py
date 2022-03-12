import os
import time
import assets
import pyautogui as pagui

os.system("color 4")

print("Hephaestus Web Search\nType 'p:' to enter private mode and 'v:' to search verbatim")
print("Query: ", end="")
reply = input().lower()
if reply != "p:" and reply != "v:":
    search = reply.split(" ")[0:]
    search = " ".join(search)

    os.startfile(assets.file_dict["dev"])
    time.sleep(2)
    pagui.hotkey("win", "up")

    pagui.hotkey("ctrl", "l")
    pagui.write(search, interval=0.001)
    pagui.press("enter")

elif reply == "p:":
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

elif reply == "v:":
    print("Query [Verbatim]: ", end="")
    reply = input().lower()
    search = reply.split(" ")[0:]
    search = " ".join(search)

    os.startfile(assets.file_dict["dev"])
    time.sleep(2)
    pagui.hotkey("win", "up")

    pagui.hotkey("ctrl", "l")
    pagui.write(f"\"{search}\"", interval=0.001)
    pagui.press("enter")