import pip
import subprocess

_all_ = [
    "SpeechRecognition>=3.8.1",
    "pynput>=1.7.2",
    "keyboard>=0.13.5",
    "google-api-python-client>=1.12.8"
]

windows = ["pywin32>=300","pipwin>=0.5.1"]

linux = []

darwin = ["AppKit>=0.2.8"]

def install(packages):
    for package in packages:
        pip.main(['install', package])

if __name__ == '__main__':

    from sys import platform
    from platform_det import Platform

    install(_all_)
    this_platform = Platform()
    this_platform.is_Linux()
    if this_platform.is_windows():
        install(windows)
        subprocess.run(["python", "-m", "pipwin", "install", "pyaudio"])
    if this_platform.is_Linux():
        install(linux)
        subprocess.run(["sudo", "apt-get", "install", "portaudio19-dev", "python3-pyaudio"])
    if platform == 'darwin': # MacOS
        install(darwin)