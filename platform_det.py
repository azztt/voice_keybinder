import sys

class Platform:
    def __init__(self):
        super().__init__()
        platforms = {
            'linux' : 'Linux',
            'linux1' : 'Linux',
            'linux2' : 'Linux',
            'darwin' : 'OS X',
            'win32' : 'Windows',
            'Windows': 'Windows',
            'cygwin': 'Windows',
        }
        if sys.platform not in platforms:
            self.platform = sys.platform
        else: 
            self.platform = platforms[sys.platform]


    def is_windows(self):
        '''Returns True is detected system is Windows else False'''
        return self.platform == "Windows"

    def is_Linux(self):
        '''Returns True is detected system is Linux else False'''
        return self.platform == "Linux"