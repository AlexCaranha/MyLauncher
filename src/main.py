from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

from kivy.properties import ObjectProperty
from kivymd.app import MDApp


class ContentNavigationDrawer123(BoxLayout):
    def build(self):
        screen_manager = ScreenManager()
        nav_drawer = ObjectProperty()

        # self.add_widget(screen_manager)
        # self.add_widget(nav_drawer)
        return self

class Main(MDApp):
    def change_title_visibility(self, enabled):
        Window.borderless = not enabled

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.change_title_visibility(False)

    def on_start(self):
        print("\non_start:")

    def on_stop(self):
        print("\non_stop:")

    def on_search_validate(self):
        print("key pressed.")

Main().run()
