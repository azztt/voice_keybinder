# Voice KeyBinder

## Voice keybinder for editors and IDEs made for programmers, by programmers

### Currently Supported Editors
1. Visual Studio Code
2. Android Studio

### Currently Supported Operating Systems
1. Windows
2. Linux
3. MacOS (Full Support coming soon!)

#### Note:-
Please ensure that your system has Python version 3.x.x installed before using this application. Download Python 3 from [here](https://www.python.org/downloads/)

### Steps to use
1. Clone this repository
2. Run ```python setup.py``` or ```python3 setup.py```
3. Run ```python main_driver.py``` or ```python3 main_driver.py```
4. Wait for initial setup before every run (Just a few seconds)
5. Now press hotkey combination to start command listener
6. Speak the command. You have only 1.5 seconds after activating the listener. This may seem less but its generally enough for speaking any command
7. You may repeat steps 5-6 as many times as you want
8. If you want to exit the application, press ctrl+shift+alt (from any window) or ctrl+c in the console

### Tunable parameters
1. Hotkey combination

#### Note:-
Please do not assign hotkey as ctrl+shift+alt. It may cause unexpected error.

### Current Limitations
1. This application uses Google Speech default API from Speech Recognition package which is temporary and may be used for testing purposes only. It may be deactivated anytime.
2. OS support for Mac is limited.
3. It does not support combinations containing clicks and numpad.
4. Only default keybindings of the supported editors can be used.

**Currently the application run only in the console/terminal. Future updates shall enable full GUI support for easier usage**