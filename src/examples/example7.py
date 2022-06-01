
from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty

from kivy.config import Config

from kivy.core.window import Window
from screeninfo import get_monitors
import pymouse

def get_center_of_current_monitor():
    mouse = pymouse.PyMouse()
    mouse_x, mouse_y = mouse.position()

    print("mouse.x: {0}, mouse.y: {1}".format(mouse_x, mouse_y))

    monitors = get_monitors()

    for iMonitor in range(0, len(monitors)):
        monitor = monitors[iMonitor]

        monitor_left = monitor.x
        monitor_right = monitor.x + monitor.width
        monitor_bottom = monitor.y
        monitor_top = monitor.y + monitor.height

        # print("monitor: {0}, width: {1}".format(iMonitor, monitor.width))
        # print("left: {0}, right: {1}".format(monitor_left, monitor_right))

        if monitor_left <= mouse_x < monitor_right and monitor_bottom <= monitor.y < monitor_top:
            # x = int((monitor_left + monitor_right)/2)
            # y = int((monitor.y + monitor.height)/2)
            x = int((monitor_right)/2)
            y = int((monitor.height)/2)
            return x, y, monitor.width, monitor.height

    return None, None, None, None

def centering_window():
    center_x, center_y, monitor_width, monitor_height = get_center_of_current_monitor()
    window_width = int(monitor_width/2)
    window_height = int(monitor_height/2)
    left = center_x - int(window_width/2)
    top = center_y - int(window_height/2)

    Config.set('graphics', 'position', 'custom')
    Config.set('graphics', 'left', left)
    Config.set('graphics', 'top', top)
    Window.size = (window_width, window_height)

centering_window()

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ScreenManager()
    nav_drawer = ObjectProperty()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue" # "Purple", "Red"
        self.theme_cls.primary_hue = "200" # "500"

        screen = MDScreen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen

MainApp().run()
