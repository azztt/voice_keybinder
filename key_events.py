# this file will contain modules for simulating key press events
from pynput.keyboard import Controller

class KeyException(Exception): pass

keyboard = Controller()

def keypress(keys):
    '''
    Input -- array of key events\n
    Function -- Simulate keypresses
    '''
    try:
        if (len(keys) == 0): return
        for key in keys:
            keyboard.press(key)
        for key in keys[::-1]:
            keyboard.release(key)
    except KeyException as e:
        print(e)