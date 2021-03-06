import os
import rich
import time
import pyvda
import ctypes
import pynput
import random
import pystray
import datetime
import keyboard
import win32gui
import pypresence
import pyautogui as pagui
from PIL import Image

user = os.getenv("username")
window_handle = win32gui.GetForegroundWindow()

file_dict = {
    "ae": rf"C:\Program Files\Adobe\Adobe After Effects 2021\Support Files\AfterFX.exe",
    "blender": r"C:\Users\{user}\Downloads\blender-2.93.6-windows-x64\blender-2.93.6-windows-x64\blender.exe",
    "cam": rf"C:\Program Files\TechSmith\Camtasia 2019\CamtasiaStudio.exe",
    "canary": rf"C:\Users\{user}\Desktop\Desktop\Discord Canary.lnk",
    "chrome": rf"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
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
    "startup": rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\startup.py",
    "test": rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\test_phase.py",
    "vsc": rf"C:\Program Files\Microsoft VS Code\Code.exe",
    "zoom": rf"C:\Users\{user}\AppData\Roaming\Zoom\bin\Zoom.exe"
}

ref_sheet = {
    "pystray": "https://pystray.readthedocs.io/en/latest/",
    "pyvda": "https://github.com/mrob95/pyvda",
    "smtp": "https://docs.python.org/3/library/smtplib.html",
    "imap": "https://docs.python.org/3/library/imaplib.html",
    "ascii": "https://ascii-generator.site/"
}

def bootup():
    """
    Opens a dialog box asking for bootup sequence
    """
    rich.print("[#00b855]Booting up[/]")
    result = pagui.confirm( text="Please select bootup mode",
                            title="Bootup Mode",
                            buttons=["Default", "Python", "Class", "Cancel"])
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

        rich.print("[#007fff]Booted up![/]")

    #CLASS
    elif box == "Class":
        startapp("Chrome", 10) #Chrome
        pagui.click(700, 570) #Click first profile
        startapp("WhatsApp", 20) #WhatsApp
        pagui.click(182, 218) #Click first chat
        pagui.click(1741, 1047) #Click chat box

        rich.print("[#007fff]Booted up![/]")

    #PYTHON
    elif box == "Python":
    #Virtual Desktop 1
        startapp("Visual Studio Code", 8) #Visual Studio Code
        startapp("Firefox Developer Edition", 8) #Firefox Developer Edition
        pagui.hotkey("alt", "tab")

        rich.print("[#007fff]Booted up![/]") 

    #CANCEL
    elif box == "Cancel":
        rich.print("[#c50f1f]Bootup canceled[/]")

def domain_check(reply):
    """
    Checks text for top-level domains
    """
    domains = ["http", ".app", ".biz", ".blog", ".com", ".dev", ".gle", ".in", ".inc", ".io", ".lol", ".ltd", ".net", ".org", ".online", ".study", ".tech", ".uk", ".us", ".wiki", ".xyz"]
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

    global key_log

    key_log = []

    def on_release(key):

        global key_log

        key_log.append(str(key))
        if len(key_log) > 3:
            del key_log[0]

        #Web Search
        if key_log == ['Key.ctrl_l', 'Key.ctrl_l', 'Key.ctrl_l']:
            try:
                win32gui.SetForegroundWindow(window_handle)
            except:
                pagui.hotkey("alt", "tab")
                win32gui.SetForegroundWindow(window_handle)
            pagui.write("/search ")
        #Screenshot
        if key_log[-1] == 'Key.print_screen':
            screenshot = pagui.screenshot()

            today = datetime.date.today()
            date = today.strftime("[%b-%d-%Y]")
            now = datetime.datetime.now()
            current_time = now.strftime("[%H-%M-%S]")

            screenshot.save(rf"C:/Users/{user}/Downloads/heph ss {current_time} {date}.png")
        #Wallpaper
        if key_log == ['Key.esc', 'Key.esc', 'Key.esc']:
            wallpapers = os.listdir(r"C:\Users\msher\Downloads\decepticon-wallpapers")
            choice = random.randint(0, len(wallpapers)-1)
            wallpaper = wallpapers[choice]
            ctypes.windll.user32.SystemParametersInfoW(20, 0, rf"C:\Users\msher\Downloads\decepticon-wallpapers\{wallpaper}", 0)
            
        if key_log == ['Key.ctrl_r', 'Key.ctrl_r', 'Key.ctrl_r']:
            wallpapers = os.listdir(r"C:\Users\msher\Desktop\Desktop\CyberFowl\Current-Project-Psd\bruh\images")
            choice = random.randint(0, len(wallpapers)-1)
            wallpaper = wallpapers[choice]
            ctypes.windll.user32.SystemParametersInfoW(20, 0, rf"C:\Users\msher\Desktop\Desktop\CyberFowl\Current-Project-Psd\bruh\images\{wallpaper}", 0)
        #Pin/Unpin
        if key_log == ['Key.shift', 'Key.shift', 'Key.shift']:
            if pyvda.AppView.current().is_pinned():
                pyvda.AppView.current().unpin()
            else:
                    pyvda.AppView.current().pin()
            key_log = []
        #Open file/app
        if key_log == ['Key.alt_l', 'Key.alt_l', 'Key.alt_l']:
            try:
                win32gui.SetForegroundWindow(window_handle)
            except:
                pagui.hotkey("alt", "tab")
                win32gui.SetForegroundWindow(window_handle)
            key_log = []
    listener = pynput.keyboard.Listener(on_release=on_release)
    listener.start()

def choose_presence():
    """
    Displays rich presence for discord
    """
    result = pagui.confirm( text="Please select bootup mode",
                            title="Bootup Mode",
                            buttons=["Python", "Work", "Cancel"])
    return result

def presence(choice):
    """
    Displays a rich presence on your Discord appliation
    """

    if choice == "Python":
        presence = pypresence.Presence("848214359822041218")
        presence.connect()
        rich.print("[#00b855]Connected[/]")
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
        rich.print("[#00b855]Connected[/]")
        work = input("Working on: ")
        presence.update(
        details=f"on {work}",
        start=time.time(),
        large_image="dnd",
        large_text="DND"
        )

    rich.print("[#007fff]Updated[/]")

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

def tray():
    """
    Runs system tray icon
    """
    global icon
    image = Image.open(rf"C:\Users\{user}\Downloads\code.png")

    def source(icon, item):
        os.system("code .")

    def github(icon, item):
        os.startfile(file_dict["dev"])
        time.sleep(2)
        pagui.hotkey("win", "up")
        pagui.hotkey("ctrl", "l")
        pagui.write("https://github.com/CyberFowl/project-hephaestus", interval=0.001)
        pagui.press("enter")

    iconMenu = pystray.Menu(pystray.MenuItem("Source code", source),
                            pystray.MenuItem("GitHub", github))
    icon = pystray.Icon("VSC", icon=image, title="Project Hephaestus", menu=iconMenu)
    icon.run_detached()

def startup():
    """
    Runs on startup of Project Hephaestus
    """
    pagui.hotkey("win", "up")
    pyvda.AppView.current().pin()
    os.system("color 4")
    keyboard.add_abbreviation('shrug', '??\_(???)_/??')
    keyboard.add_abbreviation('lamo', 'lmao')
    keyboard.add_abbreviation('burh', 'bruh')
    keyboard.add_abbreviation('SOP', 'System.out.println();')
    keyboard.add_abbreviation(':susy:', 'https://cdn.discordapp.com/emojis/888846354527428638.webp?size=32&quality=lossless')