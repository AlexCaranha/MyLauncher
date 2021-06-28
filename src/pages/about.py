
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

class About(Screen):
    def build(self):
        self.name = "AboutPage"

        label = MDLabel()
        label.text = "About"
        label.halign = "center"

        self.add_widget(label)
        print("done")
