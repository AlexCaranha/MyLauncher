from os import name
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from view_util import add_list_items_in_scroll, get_component_by_id
from kivymd.uix.list import OneLineListItem


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ScreenManager()
    nav_drawer = ObjectProperty()


class Main(MDApp):
    def change_title_visibility(self, enabled):
        Window.borderless = not enabled

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.change_title_visibility(False)

    def on_start(self):
        print("\non_start:")
        self.setup()

    def setup(self):
        self.setup_left_scroll()

    def setup_left_scroll(self):
        scroll = get_component_by_id("scroll_view", self.root)
        widgets = list()

        item1 = OneLineListItem(text="Search", on_press=self.on_press_scroll)
        item1.name="item1"
        widgets.append(item1)

        item2 = OneLineListItem(text="Configuration", on_press=self.on_press_scroll)
        item2.name="item2"

        widgets.append(item2)
        add_list_items_in_scroll(widgets, scroll)

    def on_press_scroll(self, sender):
        nav_drawer = get_component_by_id("nav_drawer", self.root)
        nav_drawer.set_state("close")

        screen_manager = get_component_by_id("screen_manager", self.root)

        if sender.name == "item1":
            screen_manager.current = "scr 1"

        if sender.name == "item2":
            screen_manager.current = "scr 2"

    def on_stop(self):
        print("\non_stop:")

    def on_search_validate(self):
        print("key pressed.")

Main().run()

# Criar função para encontrar componente recursivamente pelo id ou nome.
