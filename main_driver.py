from hotkey import hotKey
from app import App
import keyboard
import time

# hotkey for making the application listen to user
print('Select your hotkey to start listening to you. You have total 2 seconds once you start to register your hotkey.')
print('You can choose to use the default hotkey \'ctrl+shift+space\' by pressing \'ctrl+alt\' now:')
start_key_com = keyboard.read_hotkey()
if start_key_com == 'ctrl+alt':
    start_key_com = 'ctrl+shift+space'
print('Hotkey selected for starting: ' + start_key_com)

# creating new app instance
app = App()

print('\n\n\nApp ready for use. Enjoy ! (Press ctrl+shift+alt (anywhere) or ctrl+c (here in console) to exit the application)')

# now listen whenever hotkey is pressed and execute
try:
    hotKey(start_key_com, app.app)
except KeyboardInterrupt:
    print('Thank you for using this application. See you soon!')
    exit()
except Exception as e:
    print('Some unexpected error occurred... sorry for the inconvience... closing application')


print('Thank you for using this application. See you soon!')