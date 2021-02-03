from hotkey import hotKey
from app import App
import keyboard
import time

# hotkey for making the application listen to user
print('Select your hotkey to start listening to you. You can choose to use the default hotkey \'ctrl+shift+space\' by pressing \'ctrl+alt\' now:')
start_key_com = keyboard.read_hotkey()
if start_key_com == 'ctrl+alt':
    start_key_com = 'ctrl+shift+space'
print('Hotkey selected for starting: ' + start_key_com)

# creating new app instance
app = App()

print('\n\n\nApp ready for use. Enjoy ! (Press ctrl+shift+alt to exit the application)')

# now listen whenever hotkey is pressed and execute
hotKey(start_key_com, app.app)

print('Thank you for using this application. See you soon!')