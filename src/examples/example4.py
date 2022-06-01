from kivy.config import Config
Config.set('kivy', 'desktop', '1')

from kivy.app import App
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.window import Window

Clock.schedule_once(lambda *a: Window.maximize(), 2)
Clock.schedule_once(lambda *a: Window.restore(), 3)
Clock.schedule_once(lambda *a: Window.hide(), 4)
Clock.schedule_once(lambda *a: Window.show(), 5)
Clock.schedule_once(lambda *a: Window.minimize(), 6)

# class MyApp(App):

#     def on_pause(self):
#         return True

#     def build(self):
#         return Button()

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"

if __name__ == '__main__':
    MyApp().run()