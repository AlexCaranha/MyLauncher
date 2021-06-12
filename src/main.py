from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

from kivy.properties import ObjectProperty
from kivymd.app import MDApp


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ScreenManager()
    nav_drawer = ObjectProperty()


class Main(MDApp):
    def change_title_visibility(self, enabled):
        Window.borderless = not enabled

    def build(self):        
        self.theme_cls.theme_style = "Light"
        self.change_title_visibility(False)

        # self.screen.ids.screen_manager.txtSearch.bind(
        #     on_text_validate=self.on_search_validate
        # )

    def on_start(self):
        print("\non_start:")

    def on_stop(self):
        print("\non_stop:")

    def on_search_validate(self):
        print("key pressed.")

Main().run()
