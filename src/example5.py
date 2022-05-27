from tkinter import CENTER
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty

KV = '''
MDScreen:
    MDRaisedButton:
        text: "Primary Light"
        pos_hint: {"center_x": 0.5, "center_y: 0.5"}
        md_bg_color: app.theme_cls.primary_light
        
    MDRoundButton:
        text: "Primary Color"
        pos_hint: {"center_x": 0.5, "center_y: 0.5"}
        
    MDRaisedButton:
        text: "Primary Dark"
        pos_hint: {"center_x": 0.5, "center_y: 0.5"}
        md_bg_color: app.theme_cls.primary_dark
'''

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ScreenManager()
    nav_drawer = ObjectProperty()

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

MainApp().run()