import os
import glob
import time

print("Hephaestus Desktop Search\nType 'f:' to search for files and 'd:' to search for directories")
query = input()
mode = query.split(" ")[0]
if mode != "f:" and mode != "d:":
    for name in glob.glob(r"C:\Users\msher\Desktop\**\*", recursive = True):
        fd = name.split("\\")[-1]
        if query in fd:
            print(name)
            time.sleep(2)
            os.startfile(name)
            break
elif mode == "f:":
    query = query.split(" ")[1:]
    query = " ".join(query)
    for name in glob.glob(r"C:\Users\msher\Desktop\**\*", recursive = True):
        fd = name.split("\\")[-1]
        if query in fd and os.path.isfile(name):
            print(name)
            time.sleep(2)
            os.startfile(name)
            break
elif mode == "d:":
    query = query.split(" ")[1:]
    query = " ".join(query)
    for name in glob.glob(r"C:\Users\msher\Desktop\**\*", recursive = True):
        fd = name.split("\\")[-1]
        if query in fd and os.path.isdir(name):
            print(name)
            time.sleep(2)
            os.startfile(name)
            break