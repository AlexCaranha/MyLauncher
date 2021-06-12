import pyautogui

def get_monitor_size():
    width, height = pyautogui.size()
    return (width, height)

def get_percentage_of_monitor_size(
    percentage_width, percentage_height):

    width, height = pyautogui.size()
    return (width * percentage_width, height * percentage_height)
