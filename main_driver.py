from hotkey import hotKey
from app import App

# hotkey for making the application listen to user
spec_key_com = "<ctrl>+<shift>+<alt>"

# creating new app instance
app = App()

print('App ready for use. Enjoy !')

# now listen whenever hotkey is pressed and execute
# try:
hotKey(spec_key_com, app.app)
# except KeyboardInterrupt:
#     print('Thank you for using this application. See you soon!')