import os
import glob
import rich
import time
import pyvda
import assets
import random
import getpass
import smtplib
import pyautogui as pagui

assets.startup()

rich.print(r"""[#5c0dde]
 888888ba                    oo                     dP      dP     dP                    dP                                    dP                     
 88    `8b                                          88      88     88                    88                                    88                     
a88aaaa8P' 88d888b. .d8888b. dP .d8888b. .d8888b. d8888P    88aaaaa88a .d8888b. 88d888b. 88d888b. .d8888b. .d8888b. .d8888b. d8888P dP    dP .d8888b. 
 88        88'  `88 88'  `88 88 88ooood8 88'  `""   88      88     88  88ooood8 88'  `88 88'  `88 88'  `88 88ooood8 Y8ooooo.   88   88    88 Y8ooooo. 
 88        88       88.  .88 88 88.  ... 88.  ...   88      88     88  88.  ... 88.  .88 88    88 88.  .88 88.  ...       88   88   88.  .88       88 
 dP        dP       `88888P' 88 `88888P' `88888P'   dP      dP     dP  `88888P' 88Y888P' dP    dP `88888P8 `88888P' `88888P'   dP   `88888P' `88888P' 
                             88                                                 88                                                                    
                             dP                                                 dP                                                                    [/]""")

box = assets.bootup()
assets.bootup_case(box)
assets.keybind()
assets.tray()

rich.print("[#007fff]\n'/help' to access help menu[/]", end="\n\n")

console = rich.console.Console()
user = os.getenv("username")
reply = ""
while reply != "0":
    reply = input()
    plain_reply = reply
    reply = reply.lower()
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
                if int(virtual_desk) < 10:
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
                else:
                    rich.print("[#c50f1f]Wayyy too many virtual desktops[/]")

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
    elif reply == "/help":
        rich.print("""
[#007fff]Help Menu:
Features:
Type in any program to open it [#ffffff]<program name> \[virtual desktop][/#ffffff]
Type urls to web search [#ffffff]<example.(com/net/us)>[/#ffffff]

Commands:
'/boot' - enters bootup sequence
'/del [#ffffff]<file name>[/#ffffff]' - deletes [#ffffff]<file name>[/#ffffff] from downloads
'/directory [#ffffff]<query>[/#ffffff]' - searches for [#ffffff]<directory>[/#ffffff] in specified location
'/file [#ffffff]<query>[/#ffffff]' - searches for [#ffffff]<file>[/#ffffff] in specified location
'/hex [#ffffff]\[hex code][/#ffffff]' - returns [#ffffff]\[hex code][/#ffffff] preview if specified, else a random hex code with preview
'/mail' - allows you to send an email
'/music' - plays a song
'/new [#ffffff]<file name>[/#ffffff]' - creates a new file with the name [#ffffff]<file name>[/#ffffff] in downloads
'/open [#ffffff]<file name>[/#ffffff]' - opens [#ffffff]<file name>[/#ffffff] from downloads
'/path [#ffffff]<file path>[/#ffffff]' - opens [#ffffff]<file path>[/#ffffff]
'/presence' - updates discord rich presence
'[#5c0dde]/private[/#5c0dde] [#ffffff]<query>[/#ffffff]' - [#5c0dde]private[/#5c0dde] searches [#ffffff]<query>[/#ffffff] on firefox
'/reload' - reloads Project Hephaestus
'/ref [#ffffff]<doc>[/#ffffff]' - searches for [#ffffff]<doc>[/#ffffff] references
'/search [#ffffff]<query>[/#ffffff]' - searches [#ffffff]<query>[/#ffffff] on firefox
'/shutdown [#ffffff]\[time delay][/#ffffff]' - shuts down or sleeps with [#ffffff]\[time delay][/#ffffff]
'/system [#ffffff]<call>[/#ffffff]' - runs [#ffffff]<call>[/#ffffff] as system call
'/test' - enters test phase
'/xy' - returns current xy coordinates of mouse cursor
'/xycoords' - returns continuous xy coordinates of mouse cursor

Keybinds:
Press print screen to save screenshot in downloads
Press esc thrice to enter new virtual desktop
Press shift thrice to pin/unpin current window
Press ctrl thrice to activate web search[/#007fff]



[#ffffff]<> Required[/]
[#ffffff]\[] Optional[/]
""")


#Bootup
    elif reply == "/boot":
        box = assets.bootup()
        assets.bootup_case(box)

#Desktop Search
    elif reply.startswith("/file"):
        query = reply[6:]
        box = pagui.confirm(text="Select where you'd like to search",
                            title="Search Location",
                            buttons=["Desktop", "Downloads", "Documents", "Music"])
        for name in glob.glob(rf"C:\Users\{user}\{box}\**\*", recursive = True):
            fd = name.split("\\")[-1]
            if query in fd.lower() and os.path.isfile(name):
                rich.print(f"[#b6bf00]{name}[/]")
                time.sleep(2)
                os.startfile(name)
                break

    elif reply.startswith("/directory"):
        query = reply[11:]
        box = pagui.confirm(text="Select where you'd like to search",
                            title="Search Location",
                            buttons=["Desktop", "Downloads", "Documents", "Music"])
        for name in glob.glob(rf"C:\Users\{user}\{box}\**\*", recursive = True):
            fd = name.split("\\")[-1]
            if query in fd.lower() and os.path.isdir(name):
                rich.print(f"[#b6bf00]{name}[/]")
                time.sleep(2)
                os.startfile(name)
                break

#Web Search
    elif reply.startswith("/search"):
        query = reply[8:]
        os.startfile(assets.file_dict["dev"])
        time.sleep(2)
        pagui.hotkey("win", "up")

        pagui.hotkey("ctrl", "l")
        pagui.write(query, interval=0.001)
        pagui.press("enter")
        
    elif reply.startswith("/private"):
        query = reply[9:]
        os.startfile(assets.file_dict["dev"])
        time.sleep(2)
        pagui.hotkey("win", "up")

        pagui.hotkey("ctrl", "shift", "p")

        pagui.hotkey("ctrl", "l")
        pagui.write(query, interval=0.001)
        pagui.press("enter")

        time.sleep(1)

        pagui.hotkey("alt", "tab")
        pagui.hotkey("ctrl", "w")
        
#Website
    elif assets.domain_check(reply):
        os.startfile(assets.file_dict["dev"])
        time.sleep(2)
        pagui.hotkey("win", "up")

        pagui.hotkey("ctrl", "l")
        pagui.write(reply, interval=0.001)
        pagui.press("enter")

#References
    elif reply.startswith("/ref"):
        ref = reply[5:]
        if ref in assets.ref_sheet:
            pagui.write(assets.ref_sheet[ref], interval=0.01)
            time.sleep(1)
            pagui.press("enter")
        else:
            rich.print("[#c50f1f]Not found[/]")

#Gmail
    elif reply == "/mail":
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()

        rich.print(" [#007fff]Gmail ID: [/]")
        login = input(" ")
        rich.print(" [#007fff]Password: [/]", end="")
        password = getpass.getpass(prompt=" ")
        print_pass = ""
        for c in password:
            print_pass = print_pass + "*"
        print(f" {print_pass}")
        rich.print(" [#007fff]Addressee: [/]")
        adressee = input(" ")

        try:
            s.login(login, password)
            rich.print(" [#007fff]Subject: [/]")
            subject = input(" ")
            rich.print(" [#007fff]Content: [/]")
            content = input(" ")
            message = f"Subject: {subject}\n\n{content}\n\n\nSent with Project Hephaestus"
            s.sendmail(login, adressee, message)
            rich.print(f" [#00b855]Sent mail to {adressee}[/]")
            s.quit()

        except smtplib.SMTPAuthenticationError:
            rich.print(" [#c50f1f]Failed to send email. Make sure Not Secure Access is enabled on your Google Account[/]")

#Hex color
    elif reply == "/hex":
        rndm_hex = str(random.randrange(0, 16777215))[2:]
        if len(rndm_hex) != 6:
            rndm_hex = str(rndm_hex) + "0"* (6 - len(rndm_hex))
        rich.print(f"[#{rndm_hex}]██████[/] [#cccccc]#{rndm_hex}[/]")

    elif reply.startswith("/hex"):
        color = reply[-6:]
        rich.print(f"[#{color}]██████[/]")

#Music
    elif reply == "/music":
        assets.startapp("Groove", 3)
        pagui.click(397, 165)
        pagui.click(935, 549)

#Create file
    elif reply.startswith("/new"):
        file_name = reply[5:]
        open(rf"C:\Users\{user}\Downloads\{file_name}", "x")
        rich.print("[#00b855]File Created[/]")
        os.startfile(rf"C:\Users\{user}\Downloads\{file_name}")

#Open file
    elif reply.startswith("/open"):
        file_name = rf"C:\Users\{user}\Downloads\{reply[6:]}"
        if os.path.isfile(file_name):
            os.startfile(file_name)
        else:
            rich.print("[#c50f1f]File Not Found[/]")

#Delete file
    elif reply.startswith("/del"):
        file_name = rf"C:\Users\{user}\Downloads\{reply[5:]}"
        if os.path.isfile(file_name):
            os.remove(file_name)
            rich.print("[#c50f1f]File Deleted[/]")
        else:
            rich.print("[#c50f1f]File Not Found[/]")

#Path
    elif plain_reply.startswith("/path"):
        file_name = reply[6:]
        os.startfile(file_name)

#System calls
    elif reply.startswith("/system"):
        call = reply[8:]
        os.system(call)

#Presence
    elif reply == "/presence":
        choice = assets.choose_presence()
        assets.presence(choice)

#Reload
    elif reply == "/reload":
        os.startfile(assets.file_dict["startup"])
        time.sleep(1)
        pagui.hotkey("alt", "tab")
        pagui.hotkey("alt", "f4")

#Shutdown
    elif reply == "/shutdown now":
        os.system("shutdown /s /t 5")

    elif reply.startswith("/shutdown"):
        try:
            waittime = int(reply[10:])
        except ValueError:
            waittime = 5

        shutdown = console.input("[#007fff]Do you wish to shutdown your computer? (y/n): [/]")
        if shutdown == "n":
            rich.print("[#c50f1f]Shutdown sequence cancelled[/]")
        else:
            rich.print(f"[#c50f1f]Shutting down...[/]")
            time.sleep(waittime)
            rich.print("[#00b855]Shutting down now...[/]")
            time.sleep(2)
            os.system("shutdown /s /t 5")

#Sleep
    elif reply.startswith("/sleep"):
        try:
            waittime = int(reply[7:])
        except ValueError:
            waittime = 5
        
        rich.print("[#c50f1f]Entered sleep mode[/]")
        time.sleep(waittime)
        rich.print("[#00b855]Sleeping now...[/]")
        os.startfile(assets.file_dict["sleep"])

#Test space
    elif reply == "/test":
        os.startfile(assets.file_dict["test"])

#Current coords
    elif reply == "/xy":
        x, y = pagui.position()
        rich.print(f"[#c50f1f]X:{str(x).rjust(4)}[/] [#00b855]Y:{str(y).rjust(4)}[/]")

#Mouse Pointer
    elif reply == "/xycoords":
        os.startfile(assets.file_dict["mouse"])

    elif reply.startswith("/"):
        cmd = reply[1:]
        os.system(cmd)

# rich.print(f"[#5c0dde]{assets.key_log}[/]")
assets.icon.stop()