import re
# from . import keymap
import keymap

def split(text):
    '''
    Input --\n
    \ttext: str, Plain text you want to split\n
    Function -- Splits into array of array of single elements\n
    Output -- Array of array of strings
    '''
    arr = []
    arr = re.split(" ", text)
    for i in range(len(arr)):
        arr[i] = re.split("\+", arr[i])
    return arr

def map(arr):
    '''
    Input --\n
    \tarr: array of array of single elements\n
    Function -- Maps special keys to corresponding object\n
    Output -- Corrected array(To be directly used in key_events)
    '''
    for el in arr:
        for i in range(len(el)):
            if (len(el[i]) != 1):
                # el[i] = keymap[el[i]]
                el[i] = keymap.keymap[el[i]]
                continue
    return arr