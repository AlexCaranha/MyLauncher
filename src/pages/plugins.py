
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

class PluginsScreen(Screen):
    def build(self):
        self.name = "PluginsPage"

        label = MDLabel()
        label.text = "Plugins"
        label.halign = "center"

        self.add_widget(label)
        print("done")
