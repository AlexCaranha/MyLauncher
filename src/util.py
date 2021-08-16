import pyautogui
import os

def get_monitor_size():
    width, height = pyautogui.size()
    return (width, height)

def get_percentage_of_monitor_size(
    percentage_width, percentage_height):

    width, height = pyautogui.size()
    return (width * percentage_width, height * percentage_height)

def get_file_extension(file_path:str):
    file_name, file_extension = os.path.splitext(file_path)
    return file_extension

def open_file(file_path:str):
    os.startfile(file_path)

def get_file_name(file_path:str):
    return os.path.basename(file_path)

# def on_search_key_up(self, window, keycode):
#     if keycode is not None and len(keycode) == 2 and keycode[1] == "tab":
#         self.scroll.focus = True