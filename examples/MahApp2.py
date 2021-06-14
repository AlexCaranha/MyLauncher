
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

kv = '''
<BoxLayout1>:
    orientation: 'vertical'
    BoxLayout:
        size_hint_y: None
        height: 30
        id: buttons
        
    ScreenManager:
        id: sm

<MahButton>:
    on_press: app.change_screen(self.text)
'''


class MahButton(Button):
    pass


class MahApp(App):

    def change_screen(self, screen_name:str):
        self.root.ids.sm.current = screen_name

    '''
    Our main application
    '''    
    def build(self):
        # here we load the kv code, so we get the root rule as root, and
        # the MahButton dynamic class is defined
        self.root = Builder.load_string(kv)

        for l in ['a', 'b', 'c', 'd']:
            # create a screen with a Label as content, and add it to the
            # ScreenManager object, again using ids, since the rule has
            # been loaded.
            s = Screen(name=l)
            s.add_widget(Label(text=l))
            self.root.ids.sm.add_widget(s)

            # add a button with the same text as the screen name to the
            # `buttons` id of root, using the same ids technique
            self.root.ids.buttons.add_widget(MahButton(text=l))

        # we need to return the root widget
        return self.root

# common python idiom to make programs that behave well if imported as
# modules
if __name__ == '__main__':
    MahApp().run()