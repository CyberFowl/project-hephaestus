import time
import pyvda
import pyautogui as pagui

file_dict = {
    "ae": r"C:\Program Files\Adobe\Adobe After Effects 2021\Support Files\AfterFX.exe",
    "blender": r"C:\Users\msher\Downloads\blender-2.93.6-windows-x64\blender-2.93.6-windows-x64\blender.exe",
    "cam": r"C:\Program Files\TechSmith\Camtasia 2019\CamtasiaStudio.exe",
    "canary": r"C:\Users\msher\Desktop\Desktop\Discord Canary.lnk",
    "chrome": r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "discord": r"C:\Users\msher\Desktop\Desktop\Discord.lnk",
    "firefox": r"C:\Users\msher\AppData\Local\Mozilla Firefox\firefox.exe",
    "minecraft": r"C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe",
    "psd": r"C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe",
    "rec": r"C:\Program Files\TechSmith\Camtasia 2019\CamRecorder.exe",
    "slack": r"C:\Users\msher\AppData\Local\slack\slack.exe",
    "spotify": r"C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe",
    "vsc": r"C:\Program Files\Microsoft VS Code\Code.exe",
    "zoom": r"C:\Users\msher\AppData\Roaming\Zoom\bin\Zoom.exe"
}

def startapp(app_to_start, time_sleep):
    pagui.press("win")
    time.sleep(1)
    pagui.write(app_to_start, interval=0.1)
    pagui.press("enter")
    time.sleep(1)
    pagui.hotkey("win", "up")
    time.sleep(time_sleep)

def move_click(x, y):
    pagui.moveTo(x, y)
    pagui.click()

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
        move_click(295, 180) #Click first chat
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