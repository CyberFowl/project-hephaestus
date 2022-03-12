import os
import time
import pyvda
import assets
import random
import rich
import rich.console
import pyautogui as pagui
from tkinter import *

assets.startup()

print(r"""
 888888ba                    oo                     dP      dP     dP                    dP                                    dP                     
 88    `8b                                          88      88     88                    88                                    88                     
a88aaaa8P' 88d888b. .d8888b. dP .d8888b. .d8888b. d8888P    88aaaaa88a .d8888b. 88d888b. 88d888b. .d8888b. .d8888b. .d8888b. d8888P dP    dP .d8888b. 
 88        88'  `88 88'  `88 88 88ooood8 88'  `""   88      88     88  88ooood8 88'  `88 88'  `88 88'  `88 88ooood8 Y8ooooo.   88   88    88 Y8ooooo. 
 88        88       88.  .88 88 88.  ... 88.  ...   88      88     88  88.  ... 88.  .88 88    88 88.  .88 88.  ...       88   88   88.  .88       88 
 dP        dP       `88888P' 88 `88888P' `88888P'   dP      dP     dP  `88888P' 88Y888P' dP    dP `88888P8 `88888P' `88888P'   dP   `88888P' `88888P' 
                             88                                                 88                                                                    
                             dP                                                 dP                                                                    """)

box = assets.bootup()
assets.bootup_case(box)
assets.keybind()

rich.print("[#007fff]\n'/help' to access help menu[/]", end="\n\n")

console = rich.console.Console()
user = os.getenv("username")
reply = ""
while reply != "0":
    reply = input().lower()
    if not reply.startswith("/") and not assets.domain_check(reply) and not reply == "0":
        #Removing Extra Spaces
        while reply[-1] == " ":
            reply = reply[0:-1]

        #Has Virtual Desktop Specified
        try:
            program = reply.split(" ")[0:-1]
            virtual_desk = reply.split(" ")[-1]
            #Virtual Desktop open
            if int(virtual_desk) <= len(pyvda.get_virtual_desktops()):
                pyvda.VirtualDesktop(int(virtual_desk)).go()
                time.sleep(3)
                program = " ".join(program)
                #Check logged Files
                if str(program) in assets.file_dict:
                    os.startfile(assets.file_dict[program])
                #Not in Logged Files
                else:
                    assets.startapp(program, 0.1)
            #Virtual Desktop unavailable
            else:
                for i in range(0, int(virtual_desk) - len(pyvda.get_virtual_desktops())):
                    pagui.hotkey("ctrl", "win", "d")
                pyvda.VirtualDesktop(int(virtual_desk)).go()
                time.sleep(3)
                #Check logged Files
                program = " ".join(program)
                if str(program) in assets.file_dict:
                    os.startfile(assets.file_dict[program])
                #Not in Logged Files
                else:
                    assets.startapp(program, 0.1)

        #No Virtual Desktop Specified
        except ValueError:
            program = reply
            #Check logged Files
            if program in assets.file_dict:
                os.startfile(assets.file_dict[program])
            #Not in Logged Files
            else:
                assets.startapp(program, 0.1)

#Help
    elif reply.startswith("/help"):
        rich.print("""
[#007fff]Help Menu:
Features:
Type in any program to open it <(program name) (virtual desktop)>
Type urls to web search <example.(com/net/us)>

Commands:
'/boot' to enter bootup modes
'/dsearch' to enter desktop search
'/hex' to get random hex color
'/music' to play music
'/new' to create a new file
'/presence' to activate discord presence
'/reload' to reload project hephaestus
'/shutdown' to shutdown
'/sleep' to sleep
'/xy' to get current xy coordinates of mouse
'/xycoords' to get continuous xy coordinates of mouse

Keybinds:
Press esc thrice to enter new virtual desktop
Press shift thrice to pin/unpin current window
Press ctrl thrice to activate web search[/]
""")

#Website
    elif assets.domain_check(reply):
        os.startfile(assets.file_dict["web_search"])
        time.sleep(2)
        pagui.write(reply, interval=0.001)
        pagui.press("enter")

#Bootup
    elif reply.startswith("/boot"):
        box = assets.bootup()
        assets.bootup_case(box)

#Desktop Search
    elif reply.startswith("/dsearch"):
        os.startfile(assets.file_dict["desktop_search"])

#Hex color
    elif reply.startswith("/hex"):
        rndm_hex = str(random.randrange(0, 16777215))[2:]
        if len(rndm_hex) != 6:
            rndm_hex = str(rndm_hex) + "0"* (6 - len(rndm_hex))
        rich.print(f"[#{rndm_hex}]#{rndm_hex}[/]")

#Music
    elif reply.startswith("/music"):
        assets.startapp("Groove", 3)
        pagui.click(397, 165)
        pagui.click(935, 549)

#Create file
    elif reply.startswith("/new"):
        file_name = reply[5:]
        open(rf"C:\Users\{user}\Downloads\{file_name}", "x")
        os.startfile(rf"C:\Users\{user}\Downloads\{file_name}")


#Presence
    elif reply.startswith("/presence"):
        choice = assets.choose_presence()
        assets.presence(choice)

#Reload
    elif reply.startswith("/reload"):
        os.startfile(assets.file_dict["startup"])
        time.sleep(1)
        pagui.press("enter")
        time.sleep(1)
        pagui.press("left")
        pagui.press("enter")
        time.sleep(1)
        pagui.hotkey("alt", "tab")
        pagui.hotkey("alt", "f4")

#Shutdown/Sleep
    elif reply.startswith("/shutdown"):
        try:
            waittime = int(reply[10:])
        except ValueError:
            pass
        box = pagui.confirm(text="Select shutdown mode", title="Shutdown Mode", buttons=["Shutdown", "Sleep"])
        if box == "Shutdown":
            shutdown = console.input("[#007fff]Do you wish to shutdown your computer ? (y/n): [/]")
            if shutdown == "n":
                rich.print("[#c50f1f]Shutdown sequence cancelled[/]")
            else:
                rich.print(f"[#c50f1f]Shutting down in {waittime} seconds...[/]")
                time.sleep(waittime)
                print("[#00ff00]Shutting down now...[/]")
                time.sleep(2)
                os.system("shutdown /s /t 5")
        else:
            print("Entered sleep mode")
            time.sleep(waittime)
            os.startfile(assets.file_dict["sleep"])

#Test space
    elif reply.startswith("/test"):
        os.startfile(assets.file_dict["test"])

#Current coords
    elif reply.startswith("/xy"):
        x, y = pagui.position()
        print(f"X:{str(x).rjust(4)} Y:{str(y).rjust(4)}")

#Mouse Pointer
    elif reply.startswith("/xycoords"):
        os.startfile(assets.file_dict["mouse"])