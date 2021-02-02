import re
import subprocess
import speech_recognition as sr
from win32.win32gui import GetWindowText, GetForegroundWindow
from platform_det import Platform
import speech_com
from key_events import keypress
from split_map import split, map

class App:
    def __init__(self):
        super().__init__()
        this_platform = Platform()
        self.windows = this_platform.is_windows()
        self.linux = this_platform.is_Linux()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
    
    def print_empty_error(self):
        print("No editor currently in focus or command empty. You may ignore this message :)")
    
    def get_cur_window(self):
        # get window currently in focus (depends on OS)
        if self.windows:
            return GetWindowText(GetForegroundWindow())
        else:
            return subprocess.Popen(['xdotool', 'getwindowfocus', 'getwindowname'], stdout=subprocess.PIPE)
    
    def get_com(self, vsc, anst):
        command = ''

        if vsc or anst:
            command = speech_com.get_voice_command(self.r, self.m)
        command = command.replace(' ', '')
        return command.lower()
    
    def exec_command(self, key_com):
        if key_com == 'NONE':
            print('No matching command found, try something else !')
        else:
            # getting proper formatted array key combination
            key_com = map(split(key_com))

            # executing the key combination command
            for el in key_com:
                keypress(el)
    
    def app(self):

        print("hot key pressed !")
        # get focused window
        cur_window = self.get_cur_window()

        # check if vs code is in focus
        vsc = len(re.findall(r'Visual Studio Code$', cur_window)) > 0
        
        # check if android studio is in focus
        anst = len(re.findall(r'Android Studio$', cur_window)) > 0

        # get the voice command
        command = self.get_com(vsc, anst)

        key_com = ''

        # if command is not empty
        if not(command == ''):
            if vsc:
                # importing for vs code commands
                from vscode_bind import get_key_com

                key_com = get_key_com(command)
                # print(key_com)
            elif anst:
                # importing for android studio commands
                from android_bind import get_key_com
                key_com = get_key_com(command)
            
            self.exec_command(key_com)
        else:
            self.print_empty_error()