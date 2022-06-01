import pyautogui
import subprocess, os, platform

import mss

def get_monitor_size():
    sct = mss.mss()
    primary_monitor = sct.monitors[1]

    return (primary_monitor['width'], primary_monitor['height'])

def get_percentage_of_monitor_size(
    percentage_width, percentage_height):

    width, height = get_monitor_size()
    return (width * percentage_width, height * percentage_height)

def get_file_extension(file_path:str):
    file_name, file_extension = os.path.splitext(file_path)
    return file_extension

def open_file(file_path:str):
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', file_path))

    elif platform.system() == 'Windows':    # Windows
        subprocess.call(('open', file_path))
        
    else:                                   # linux variants
        subprocess.call(('xdg-open', file_path))

def get_file_name(file_path:str):
    return os.path.basename(file_path)

def is_blank (myString):
    return not (myString and myString.strip())

def is_not_blank (myString):
    return bool(myString and myString.strip())

# def on_search_key_up(self, window, keycode):
#     if keycode is not None and len(keycode) == 2 and keycode[1] == "tab":
#         self.scroll.focus = True

# PyUserInput==0.1.11
# screeninfo==0.8