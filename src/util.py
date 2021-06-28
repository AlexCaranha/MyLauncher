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
