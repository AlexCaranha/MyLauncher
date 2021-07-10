
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

class ExitScreen(Screen):
    def build(self):
        self.name = "ExitPage"

        label = MDLabel()
        label.text = "Exit"
        label.halign = "center"

        self.add_widget(label)
        print("done")
