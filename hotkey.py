# from pynput import keyboard
import keyboard

class HotKeyException(Exception): pass

def hotKey(key_on, press_fn):
    '''
    Input --\n
    \tkey_on: str, key combination for hotkey\n
    \tpress_fn: function, function to be executed on pressing hotkey\n
    Function -- adds a hotkey pressing fn
    '''
    try:
        keyboard.add_hotkey(key_on, press_fn)
        keyboard.wait('ctrl+shift+alt')
        keyboard.remove_hotkey(key_on)
    except HotKeyException as e:
        print('An unexpected error occured... sorry for the inconvenience. Closing the application')
        keyboard.release(key_on)
        keyboard.remove_hotkey(key_on)
    