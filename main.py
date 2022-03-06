import os
import time
import pyvda
import assets
import random
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
assets.keybind()

print()
print("'help:' to access help menu")
print()

reply = ""

while reply != "0":
    reply = input().lower()
    commands = ["help:", "0", "boot:", "dsearch:", "hex:", "music:", "new:", "presence:", "shutdown:", "sleep:", "test:", "xy:", "xycoords:"]
    if reply not in commands and not assets.domain_check(reply):
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
    elif reply == "help:":
        print("""Help Menu:
Features:
Type in any program to open it <[program name] (virtual desktop)>
Type urls to web search <example.[com/net/us]>

Commands:
'boot:' to enter bootup modes
'dsearch:' to enter desktop search
'hex:' to get random hex color
'music:' to play music
'new:' to create a new file
'presence:' to activate discord presence
'shutdown:' to shutdown
'sleep:' to sleep
'xy:' to get current xy coordinates of mouse
'xycoords:' to get continuous xy coordinates of mouse

Keybinds:
Press esc thrice to enter new virtual desktop
Press shift thrice to pin/unpin current window
Press ctrl thrice to activate web search
""")

#Website
    elif assets.domain_check(reply):
        os.startfile(assets.file_dict["web_search"])
        time.sleep(2)
        pagui.write(reply, interval=0.001)
        pagui.press("enter")

#Bootup
    elif reply == "boot:":
        box = assets.bootup()
        assets.bootup_case(box)

#Desktop Search
    elif reply == "dsearch:":
        os.startfile(assets.file_dict["desktop_search"])

#Random color
    elif reply == "hex:":
        rndm_hex = str(random.randrange(0, 16777215))
        rndm_hex = rndm_hex[2:]
        if len(rndm_hex) != 6:
            rndm_hex = str(rndm_hex) + "0"* (6 - len(rndm_hex))
        print(f"#{rndm_hex}")
        time.sleep(1)
        os.startfile(assets.file_dict["web_search"])
        time.sleep(1)
        pagui.write(f"#{rndm_hex}")
        pagui.press("enter")

#Music
    elif reply == "music:":
        assets.startapp("Groove", 3)
        pagui.click(397, 165)
        pagui.click(935, 549)

#Create file
    elif reply == "new:":
        file_name = input("File name: ")
        open(rf"C:\Users\msher\Downloads\{file_name}", "x")
        os.startfile(rf"C:\Users\msher\Downloads\{file_name}")


#Presence
    elif reply == "presence:":
        choice = assets.choose_presence()
        assets.presence(choice)

#Shutdown
    elif reply == "shutdown:":
        shutdown = input("Do you wish to shutdown your computer ? (y/n): ")
        if shutdown == "n":
            print("Shutdown sequence cancelled")
        else:
            print("Shutting down now...")
            time.sleep(1)
            os.system("shutdown /s /t 5")

#Sleep
    elif reply == "sleep:":
        os.startfile(assets.file_dict["sleep"])

#Test space
    elif reply == "test:":
        os.startfile(assets.file_dict["test"])

#Current coords
    elif reply == "xy:":
        x, y = pagui.position()
        print(f"X:{str(x).rjust(4)} Y:{str(y).rjust(4)}")

#Mouse Pointer
    elif reply == "xycoords:":
        os.startfile(assets.file_dict["mouse"])