import os
import time
import pyvda
import pynput
import keyboard
import pyautogui as pagui

user = os.getenv("username")

file_dict = {
    "ae": rf"C:\Program Files\Adobe\Adobe After Effects 2021\Support Files\AfterFX.exe",
    "blender": r"C:\Users\{user}\Downloads\blender-2.93.6-windows-x64\blender-2.93.6-windows-x64\blender.exe",
    "cam": rf"C:\Program Files\TechSmith\Camtasia 2019\CamtasiaStudio.exe",
    "canary": rf"C:\Users\{user}\Desktop\Desktop\Discord Canary.lnk",
    "chrome": rf"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "discord": rf"C:\Users\{user}\Desktop\Desktop\Discord.lnk",
    "firefox": rf"C:\Users\{user}\AppData\Local\Mozilla Firefox\firefox.exe",
    "dev": rf"C:\Program Files\Firefox Developer Edition\firefox.exe",
    "key": rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\key.py",
    "minecraft": rf"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe",
    "mouse": rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\mouse-pointer.py",
    "psd": rf"C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe",
    "rec": rf"C:\Program Files\TechSmith\Camtasia 2019\CamRecorder.exe",
    "slack": rf"C:\Users\{user}\AppData\Local\slack\slack.exe",
    "spotify": rf"C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe",
    "vsc": rf"C:\Program Files\Microsoft VS Code\Code.exe",
    "zoom": rf"C:\Users\{user}\AppData\Roaming\Zoom\bin\Zoom.exe"
}

def bootup():
    print("Booting up")
    result = pagui.confirm(text="Please select bootup mode", title="Bootup Mode", buttons=["Default", "Python", "Class", "Cancel"])
    return result
    
def bootup_case(box):
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
        move_click(182, 218) #Click first chat
        move_click(1741, 1047) #Click chat box

        print("Booted up!")

    #CLASS
    elif box == "Class":
        startapp("Chrome", 10) #Chrome
        move_click(700, 570) #Click first profile
        startapp("WhatsApp", 20) #WhatsApp
        move_click(182, 218) #Click first chat
        move_click(1741, 1047) #Click chat box

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

def move_click(x, y):
    pagui.moveTo(x, y)
    pagui.click()

def keybind():
    ctrl_l_count = 0
    esc_count = 0
    shift_l_count = 0
    def on_release(key):
        #Search
        global ctrl_l_count, esc_count, shift_l_count
        if key == pynput.keyboard.Key.ctrl_l:
            ctrl_l_count += 1
            if ctrl_l_count == 3:
                os.startfile(rf"C:\Users\{user}\Desktop\Desktop\project-hephaestus\search.py")
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
    listener = pynput.keyboard.Listener(on_release=on_release)
    listener.start()

def startapp(app_to_start, time_sleep):
    pagui.press("win")
    time.sleep(1)
    pagui.write(app_to_start, interval=0.1)
    pagui.press("enter")
    time.sleep(1)
    pagui.hotkey("win", "up")
    time.sleep(time_sleep)

def startup():
    pagui.hotkey("win", "up")
    pyvda.AppView.current().pin()
    keyboard.add_abbreviation('shrug', '¯\_(ツ)_/¯')
    keyboard.add_abbreviation('lamo', 'lmao')