import os
import glob
import time
import pyautogui as pagui

os.system("color 4")
query = input("Hephaestus Desktop Search\nType 'f:' to search for files and 'd:' to search for directories\nQuery: ")
mode = query.split(" ")[0]

user = os.getenv("username")
box = pagui.confirm(text="Select where you'd like to search", title="Search Location", buttons=["Desktop", "Downloads", "Documents", "Music"])

if mode != "f:" and mode != "d:":
    for name in glob.glob(rf"C:\Users\{user}\{box}\**\*", recursive = True):
        fd = name.split("\\")[-1]
        if query in fd:
            print(name)
            time.sleep(2)
            os.startfile(name)
            break
elif mode == "f:":
    query = query.split(" ")[1:]
    query = " ".join(query)
    for name in glob.glob(rf"C:\Users\{user}\{box}\**\*", recursive = True):
        fd = name.split("\\")[-1]
        if query in fd and os.path.isfile(name):
            print(name)
            time.sleep(2)
            os.startfile(name)
            break
elif mode == "d:":
    query = query.split(" ")[1:]
    query = " ".join(query)
    for name in glob.glob(rf"C:\Users\{user}\{box}\**\*", recursive = True):
        fd = name.split("\\")[-1]
        if query in fd and os.path.isdir(name):
            print(name)
            time.sleep(2)
            os.startfile(name)
            break