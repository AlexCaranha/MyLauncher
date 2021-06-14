from os import name
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder


from view_util import create_scroll_list_items
from kivymd.uix.list import OneLineListItem

class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        widgets = list()
        widgets.append(OneLineListItem(text="item 1", on_press=self.do_print))
        widgets.append(OneLineListItem(text="item 2", on_press=self.do_print))
        widgets.append(OneLineListItem(text="item 3", on_press=self.do_print))

        scroll = create_scroll_list_items(widgets)

        screen.add_widget(scroll)
        return screen

    def do_print(self, sender):
        return print(f'clicked: {sender.text}')


DemoApp().run()