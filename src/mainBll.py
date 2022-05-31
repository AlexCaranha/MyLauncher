
from util import get_percentage_of_monitor_size, get_monitor_size

from kivy.core.window import Window
from pynput import keyboard

from kivy.clock import Clock

window_hide = False
keys_pressed = []

def show_hide_window():
    global window_hide
    window_hide = not window_hide

    if window_hide:
        Clock.schedule_once(lambda *a: Window.hide(), 0)

    else:
        Clock.schedule_once(lambda *a: Window.show(), 0)

    print("done.")

def on_press(key):
    if hasattr(key, 'name'):
        keys_pressed.append(key.name)

    if 'space' in keys_pressed and 'ctrl' in keys_pressed and 'alt' in keys_pressed:            
        show_hide_window()    

def on_release(key):
    if hasattr(key, 'name'):
        keys_pressed.remove(key.name)

def keyboard_listener():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)

    listener.window_hide = False
    listener.start()

def window_locate():
    (width, height) = get_percentage_of_monitor_size(0.5, 0.5)
    Window.size = (width, height)

    Window.left = width - width/2
    Window.top = height - height/2