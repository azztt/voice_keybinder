# Voice KeyBinder

## First voice keybinder for editors made for programmers, by programmers

### Supported Editors
1. Visual Studio Code
2. Android Studio

### Supported OS
1. Windows
2. Linux
3. MacOS (Full Support coming soon!)

#### Note:-
Please install python3.x.x before proceeding further. [Python3 Link](https://www.python.org/downloads/)

### Steps to use
1. Clone this repo
2. Run ```pip install -r requirements.txt```
3. Run ```python main_driver.py```
4. Wait for initial setup
5. Now press hotkey combination to start listener
6. Speak the command
7. After the execution of command, if you want to again speak another command, again press the hotkey.
8. If you want to exit the application, press ctrl+shift+alt

### Tunable parameters
1. Hotkey combination
2. Speak Timer (Not more than 2 seconds)

#### Note:-
Please do not assign hotkey as ctrl+shift+alt. It may cause unexpected error.

### Limitations
1. This application uses Google Speech API which usage is limited due to non-free cost.
2. OS support for Mac is limited.
3. It does not support combination containing clicks and numpad.