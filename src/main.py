from os import name
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager

from kivy.properties import ObjectProperty
from kivymd.app import MDApp

from view_util import add_list_items_in_scroll, get_component_by_id

from kivymd.uix.list import OneLineListItem

from pages.about import AboutScreen
from pages.configuration import ConfigurationScreen
from pages.search import SearchScreen
from pages.exit import ExitScreen
from pages.plugins import PluginsScreen

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ScreenManager()
    nav_drawer = ObjectProperty()

class Main(MDApp):
    def change_title_visibility(self, enabled):
        Window.borderless = not enabled

    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.change_title_visibility(False)

    def on_start(self):
        print("\non_start:")
        self.setup()

    def setup(self):
        self.setup_screens()
        self.setup_left_scroll()

    def setup_screens(self):
        screen_manager = get_component_by_id("screen_manager", self.root)

        screens = [ConfigurationScreen(), SearchScreen(), AboutScreen(), PluginsScreen(), ExitScreen()]

        for screen in screens:
            screen.build()
            screen_manager.add_widget(screen)

        screen_manager.current = "SearchPage"

    def setup_left_scroll(self):
        scroll = get_component_by_id("scroll_view", self.root)
        widgets = list()

        dictionary = self.get_dictionary_pages()

        for key, value in dictionary.items():            
            item = OneLineListItem(text=value[0], on_press=self.on_press_scroll)
            item.name=key
            widgets.append(item)
        
        add_list_items_in_scroll(widgets, scroll)

    def on_press_scroll(self, sender):
        nav_drawer = get_component_by_id("nav_drawer", self.root)
        nav_drawer.set_state("close")

        screen_manager = get_component_by_id("screen_manager", self.root)
        dictionary = self.get_dictionary_pages()

        if sender.name in dictionary:
            screen_manager.current = dictionary[sender.name][1]

    def on_stop(self):
        print("\non_stop:")

    def get_dictionary_pages(self):
        dictionary = {
            "itemSearch": ("Search", "SearchPage"),
            "itemConfiguration": ("Configuration", "ConfigurationPage"),
            "itemPlugins": ("Plugins", "PluginsPage"),
            "itemAbout": ("About", "AboutPage"),
            "itemExit": ("Exit", "ExitPage"),
        }
        return dictionary

Main().run()