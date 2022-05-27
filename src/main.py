# from turtle import Screen
from kivy.base import runTouchApp

from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

from view_util import add_list_items_in_scroll, get_component_by_id

from pages.about import AboutScreen
from pages.configuration import ConfigurationScreen
from pages.search import SearchScreen
from pages.exit import ExitScreen
from pages.plugins import PluginsScreen

from plugins.manager import Manager
from hotkey import HotKeyBehavior

from datetime import datetime

print("Instanciando Plugin Manager.")
manager = Manager()

print("Carregando plugins.")
manager.load_plugins()

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ScreenManager()
    nav_drawer = ObjectProperty()


class Main(HotKeyBehavior, MDApp):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        # self.key_exit = "ctrl+c"
        self.key_show="ctrl+shift+space"
        self.on_parent(self, Window)
        # self.build()

    def change_title_visibility(self, enabled):
        Window.borderless = not enabled
        print("change_title_visibility ...")

    def build(self):
        # self.root = Builder.load_file("main.kv")
        self.icon = "assets\\rocket.png"
        # self.theme_cls.theme_style = "Dark"
        self.change_title_visibility(False)
        # Window.bind(on_key_down=self._keydown)
        # Window.bind(on_key_up=self._keyup)

        # Window.bind(on_key_down=self._on_keyboard_down)
        # Window.bind(on_key_up=self._on_keyboard_up)
        # self.on_start()

    def on_press(self):
        pass

    def on_show(self):
        self.now_show = datetime.now()

    def on_hide(self):
        self.now_hide = datetime.now()
    

    # def _keydown(self, window, key, scancode, codepoint, modifiers):
    #     print('keydown:')
    #     print('\tkey:',key)
    #     print('\tscancode:', scancode)
    #     print('\tcodepoint:', codepoint)
    #     print('\tmodifiers:', modifiers)

    # def _keyup(self, window, key, scancode):
    #     print('keyup:')
    #     print('\tkey:',key)
    #     print('\tscancode:', scancode)

    def _on_keyboard_down(self, *args):
        print(f'down: {args}')

    def _on_keyboard_up(self, *args):
        print(f'up: {args}')

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
        # print("on_stop:")
        pass

    def get_dictionary_pages(self):
        dictionary = {
            "itemSearch": ("Search", "SearchPage"),
            "itemConfiguration": ("Configuration", "ConfigurationPage"),
            "itemPlugins": ("Plugins", "PluginsPage"),
            "itemAbout": ("About", "AboutPage"),
            "itemExit": ("Exit", "ExitPage"),
        }
        return dictionary

if __name__ == "__main__":
    Main().run()
    # runTouchApp(Main())

# Main().run()