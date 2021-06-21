from os import name
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

from kivy.properties import ObjectProperty
from kivymd.app import MDApp

from view_util import add_list_items_in_scroll, get_component_by_id

from kivymd.uix.list import OneLineListItem
from pages.configuration import Configuration
from pages.search import Search

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
        self.setup_screens()
        self.setup_left_scroll()

    def setup_screens(self):
        screen_manager = get_component_by_id("screen_manager", self.root)

        screen = Configuration()
        screen.build()
        screen_manager.add_widget(screen)

        screen = Search()
        screen.build()
        screen_manager.add_widget(screen)

        screen_manager.current = "SearchPage"

    def setup_left_scroll(self):
        scroll = get_component_by_id("scroll_view", self.root)
        widgets = list()

        item = OneLineListItem(text="Search", on_press=self.on_press_scroll)
        item.name="itemSearch"
        widgets.append(item)

        item = OneLineListItem(text="Configuration", on_press=self.on_press_scroll)
        item.name="itemConfiguration"

        widgets.append(item)
        add_list_items_in_scroll(widgets, scroll)

    def on_press_scroll(self, sender):
        nav_drawer = get_component_by_id("nav_drawer", self.root)
        nav_drawer.set_state("close")

        screen_manager = get_component_by_id("screen_manager", self.root)

        if sender.name == "itemSearch":
            screen_manager.current = "SearchPage"

        if sender.name == "itemConfiguration":
            screen_manager.current = "ConfigurationPage"

    def on_stop(self):
        print("\non_stop:")

Main().run()

# Criar função para encontrar componente recursivamente pelo id ou nome.
