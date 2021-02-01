import re
# from . import keymap
import keymap

def split(text):
    '''
    Input -- plain text you want to split
    Function -- Splits into array of array of single elements
    Output -- Array of array of strings
    '''
    arr = []
    arr = re.split(" ", text)
    for i in range(len(arr)):
        arr[i] = re.split("\+", arr[i])
    return arr

def map(arr):
    '''
    Input -- Splits into array of array of single elements
    Function -- Maps special keys to corresponding object
    Output -- Corrected array(To be directly used in key_events)
    '''
    for el in arr:
        for i in range(len(el)):
            if (len(el[i]) != 1):
                # el[i] = keymap[el[i]]
                el[i] = keymap.keymap[el[i]]
                continue
    return arr