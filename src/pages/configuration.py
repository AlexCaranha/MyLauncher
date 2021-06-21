
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

class Configuration(Screen):
    def build(self):
        self.name = "ConfigurationPage"

        label = MDLabel()
        label.text = "Configuration"
        label.halign = "center"

        self.add_widget(label)
        print("done")
