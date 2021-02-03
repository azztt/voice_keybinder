from hotkey import hotKey
from app import App
import keyboard
import time
from cfonts import render

# App Name :)
output = render('Voice Keybinder', align='center')
print(output)


try:
    # hotkey for making the application listen to user
    print('Select your hotkey to start listening to you. Beware it should not match any other shortcut of your editor.')
    print('You can choose to use the default hotkey \'ctrl+shift+windows\' by pressing \'ctrl+alt\' now:')
    start_key_com = keyboard.read_hotkey()
    if start_key_com == 'ctrl+alt' or start_key_com == 'ctrl+shift+alt':
        start_key_com = 'ctrl+shift+windows'
    print('Hotkey selected for starting: ' + start_key_com)

    # # time to speak command
    # speak_time = int(input('Enter time in seconds you need to speak commands (maximum 2.5 seconds): '))
    # speak_time = speak_time if speak_time <= 2.5 else 2.5
    # print('Time to speak each command: {} seconds'.format(speak_time))

    # creating new app instance
    app = App()

    print('\n\n\nApp ready for use. Enjoy ! (Press ctrl+shift+alt (anywhere) or ctrl+c (here in console) to exit the application)')
except KeyboardInterrupt:
    print('Thank you for using this application. See you soon!')
    exit()


# now listen whenever hotkey is pressed and execute
try:
    hotKey(start_key_com, app.app)
except KeyboardInterrupt:
    print('Thank you for using this application. See you soon!')
    exit()
except Exception as e:
    print('Some unexpected error occurred... sorry for the inconvience... closing application')


print('Thank you for using this application. See you soon!')