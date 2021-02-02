from pynput import keyboard

class HotKeyException(Exception): pass

def hotKey(key, press_fn):
    '''
    Input:
    key -- key combination for hotkey eg- '<ctrl>+<alt>+h'
    press_fn -- function to be executed on pressing hotkey
    Function -- adds a hotkey pressing fn
    '''
    try:
        # def for_canonical(f):
        #     return lambda k: f(l.canonical(k))
        # hotkey = keyboard.HotKey(
        # keyboard.HotKey.parse(key),
        # press_fn)
        # with keyboard.Listener(
        #     on_press=for_canonical(hotkey.press),
        #     on_release=for_canonical(hotkey.release)) as l:
        #     l.join()
        with keyboard.GlobalHotKeys({
                key: press_fn}) as h:
            h.join()
    except HotKeyException as e:
        print(e)