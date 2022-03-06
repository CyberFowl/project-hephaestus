import os
import time
import pyvda
import pynput
import keyboard
import win32gui
import pypresence
import pyautogui as pagui

user = os.getenv("username")
window_handle = win32gui.GetForegroundWindow()

file_dict = {
    "ae": rf"C:\Program Files\Adobe\Adobe After Effects 2021\Support Files\AfterFX.exe",
    "blender": r"C:\Users\{user}\Downloads\blender-2.93.6-windows-x64\blender-2.93.6-windows-x64\blender.exe",
    "cam": rf"C:\Program Files\TechSmith\Camtasia 2019\CamtasiaStudio.exe",
    "canary": rf"C:\Users\{user}\Desktop\Desktop\Discord Canary.lnk",
    "chrome": rf"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "desktop_search": rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\desktop_search.py",
    "discord": rf"C:\Users\{user}\Desktop\Desktop\Discord.lnk",
    "firefox": rf"C:\Users\{user}\AppData\Local\Mozilla Firefox\firefox.exe",
    "dev": rf"C:\Program Files\Firefox Developer Edition\firefox.exe",
    "minecraft": rf"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe",
    "mouse": rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\mouse-pointer.py",
    "psd": rf"C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe",
    "rec": rf"C:\Program Files\TechSmith\Camtasia 2019\CamRecorder.exe",
    "slack": rf"C:\Users\{user}\AppData\Local\slack\slack.exe",
    "sleep": rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\sleep.py",
    "spotify": rf"C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe",
    "test": rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\test_phase.py",
    "vsc": rf"C:\Program Files\Microsoft VS Code\Code.exe",
    "web_search": rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\web_search.py",
    "zoom": rf"C:\Users\{user}\AppData\Roaming\Zoom\bin\Zoom.exe"
}

def bootup():
    """
    Opens a dialog box asking for bootup sequence
    """
    print("Booting up")
    result = pagui.confirm(text="Please select bootup mode", title="Bootup Mode", buttons=["Default", "Python", "Class", "Cancel"])
    return result
    
def bootup_case(box):
    """
    Runs a bootup sequence based on `bootup()`
    """
    if box == "Default":
    #Virtual Desktop 1
        startapp("Firefox", 14) #Firefox
        startapp("Visual Studio Code", 8) #Visual Studio Code

    #Virtual Desktop 2
        if 2 <= len(pyvda.get_virtual_desktops()):
            pyvda.VirtualDesktop(2).go()
            time.sleep(2)
        else:
            for i in range(0, 2 - len(pyvda.get_virtual_desktops())):
                pagui.hotkey("ctrl", "win", "d")
            pyvda.VirtualDesktop(2).go()
            time.sleep(2)

        startapp("Canary", 17) #Canary
        startapp("WhatsApp", 20) #WhatsApp
        pagui.click(182, 218) #Click first chat
        pagui.click(1741, 1047) #Click chat box

        print("Booted up!")

    #CLASS
    elif box == "Class":
        startapp("Chrome", 10) #Chrome
        pagui.click(700, 570) #Click first profile
        startapp("WhatsApp", 20) #WhatsApp
        pagui.click(182, 218) #Click first chat
        pagui.click(1741, 1047) #Click chat box

        print("Booted up!")

    #PYTHON
    elif box == "Python":
    #Virtual Desktop 1
        startapp("Visual Studio Code", 8) #Visual Studio Code
        startapp("Firefox Developer Edition", 8) #Firefox Developer Edition
        pagui.hotkey("alt", "tab")

        print("Booted up!") 

    #CANCEL
    elif box == "Cancel":
        print("Bootup canceled")

def domain_check(reply):
    """
    Checks text for top-level domains
    """
    domains = [".app", ".biz", ".blog", ".com", ".dev", ".gle", ".in", ".inc", ".lol", ".ltd", ".net", ".org", ".online", ".study", ".tech", ".uk", ".us", ".wiki", ".xyz"]
    for domain in domains:
        if domain in reply:
            state = True
            break
        else:
            state = False

    return state

def keybind():
    """
    Waits for key combinations to run code
    """
    ctrl_l_count = 0
    esc_count = 0
    shift_l_count = 0
    alt_l_count = 0
    def on_release(key):
        #Web Search
        global ctrl_l_count, esc_count, shift_l_count, alt_l_count
        if key == pynput.keyboard.Key.ctrl_l:
            ctrl_l_count += 1
            if ctrl_l_count == 3:
                os.startfile(rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\web_search.py")
        else:
            ctrl_l_count = 0
        #Escape
        if key == pynput.keyboard.Key.esc:
            esc_count += 1
            if esc_count == 3:
                pyvda.AppView.current().unpin()
                pagui.hotkey("ctrl","win","d")
        else:
            esc_count = 0
        #Pin/Unpin
        if key == pynput.keyboard.Key.shift_l:
            shift_l_count += 1
            if shift_l_count == 3:
                if pyvda.AppView.current().is_pinned():
                    pyvda.AppView.current().unpin()
                else:
                    pyvda.AppView.current().pin()
        else:
            shift_l_count = 0
        # #Open file/app
        # if key == pynput.keyboard.Key.alt_l:
        #     alt_l_count += 1
        #     if alt_l_count == 3:
        #         win32gui.SetForegroundWindow(window_handle)
        #         pyvda.AppView.current().pin()
        # else:
        #     alt_l_count = 0
    listener = pynput.keyboard.Listener(on_release=on_release)
    listener.start()

def choose_presence():
    """
    Displays rich presence for discord
    """
    result = pagui.confirm(text="Please select bootup mode", title="Bootup Mode", buttons=["Python", "Work", "Cancel"])
    return result

def presence(choice):
    """
    Displays a rich presence on your Discord appliation
    """

    if choice == "Python":
        presence = pypresence.Presence("848214359822041218")
        presence.connect()
        print("Connected")
        presence.update(
        details="on vs code",
        large_image="python",
        small_image="vsc",
        large_text="Project Hephaestus",
        small_text="Visual Studio Code",
        buttons=[
                {"label": "GitHub",
                "url": "https://github.com/CyberFowl/"},
                {"label": "Current Project",
                "url": "https://github.com/CyberFowl/project-hephaestus/"}
                ]
        )
    
    elif choice == "Work":
        presence = pypresence.Presence("946448728884138014")
        presence.connect()
        print("Connected")
        work = input("Working on: ")
        presence.update(
        details=f"on {work}",
        start=time.time(),
        large_image="dnd",
        large_text="DND"
        )

    print("Updated")

def startapp(app_to_start, time_sleep):
    """
    Starts an app from start search bar with an interval of `x` seconds
    """
    pagui.press("win")
    time.sleep(1)
    pagui.write(app_to_start, interval=0.1)
    pagui.press("enter")
    time.sleep(1)
    pagui.hotkey("win", "up")
    time.sleep(time_sleep)

def startup():
    """
    Runs on startup of Project Hephaestus
    """
    pagui.hotkey("win", "up")
    pyvda.AppView.current().pin()
    keyboard.add_abbreviation('shrug', '¯\_(ツ)_/¯')
    keyboard.add_abbreviation('lamo', 'lmao')
    keyboard.add_abbreviation('burh', 'bruh')
    keyboard.add_abbreviation('SOP', 'System.out.println();')
    keyboard.add_abbreviation(':susy:', 'https://cdn.discordapp.com/emojis/888846354527428638.webp?size=32&quality=lossless')