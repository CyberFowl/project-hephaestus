import os
import time
import pyvda
import assets
import pyglet
import random
import shutil
import test_phase
import pyautogui as pagui

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

print()
print("""Commands:
's: <query>' to search
'm:' to play music
'p:' or 'pin:' to pin current window [3 second delay]
'up:' or 'unpin:' to unpin current window [3 second delay]""")
print()

reply = ""

while reply != "0":
    reply = input().lower()
    commands = ["0", "m:", "music", "p:", "pin:", "up:", "unpin:", "b:", "bootup:", "t:", "test:"]
    if reply not in commands and not reply.startswith("s: "):
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
                    assets.startapp(" ".join(program), 0.1)
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
                    assets.startapp(" ".join(program), 0.1)

        #No Virtual Desktop Specified
        except ValueError:
            program = reply
            #Check logged Files
            if program in assets.file_dict:
                os.startfile(assets.file_dict[program])
            #Not in Logged Files
            else:
                assets.startapp(program, 0.1)

#Search
    elif reply.startswith("s: "):
        search = reply.split(" ")[1:]
        search = " ".join(search)

        pagui.hotkey("win", "shift", "3")
        time.sleep(2)

        pagui.hotkey("ctrl", "l")
        pagui.write(search, interval=0.001)
        pagui.press("enter")

#Pin Window
    elif reply == "p:" or reply == "pin:":
        time.sleep(3)
        pyvda.AppView.current().pin()
        print("Pinned")

#Unpin Window
    elif reply == "up:" or reply == "unpin:":
        time.sleep(3)
        pyvda.AppView.current().unpin()
        print("Unpinned")

#Bootup
    elif reply == "b:" or reply == "bootup:":
        box = assets.bootup()
        assets.bootup_case(box)

#Music
    elif reply == "m:" or reply == "music:":
        assets.startapp("Groove", 3)
        assets.move_click(397, 165)
        assets.move_click(935, 549)

#Test space
    elif reply == "t:" or reply == "test:":
        test_phase.test()