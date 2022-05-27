import win32gui
import win32con


def main():
    while True:
        c_out = input(f"Enter command: ")
        if c_out.lower() == 'hide':
            window('hide')


def window(mode: str):
    the_program_to_hide = win32gui.GetForegroundWindow()
    if mode == 'show':
        win32gui.ShowWindow(the_program_to_hide, win32con.SW_SHOW)
    else:
        win32gui.ShowWindow(the_program_to_hide, win32con.SW_HIDE)


main()