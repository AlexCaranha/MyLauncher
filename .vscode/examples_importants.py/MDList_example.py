
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
ScrollView:
    MDList:
        TwoLineListItem:
            text: "Item 1"
            secondary_text: "Secondary text 1"
            on_release: print("Click!")            

        TwoLineListItem:
            text: "Item 2"
            secondary_text: "Secondary text 2"
            on_release: print("Click 2!")            
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
