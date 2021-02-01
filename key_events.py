# this file will contains modules for simulating key press events
from pynput.keyboard import Key, Controller
import time
keyboar = Controller()

def keypress(keys):
    time.sleep(2)
    if (len(keys) == 0): return
    for key in keys:
        keyboar.press(key)
    time.sleep(2)
    for key in keys[::-1]:
        keyboar.release(key)