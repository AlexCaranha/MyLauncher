
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

class Search(Screen):
    def build(self):
        self.name = "SearchPage"

        txtSearch = MDTextField()
        txtSearch.name = "txtSearch"
        txtSearch.hint_text = "How can I help you?"
        txtSearch.mode = "rectangle"
        txtSearch.pos_hint = {"center_x": .5, "center_y": .80}
        txtSearch.size_hint_x = 0.95
        txtSearch.focus = True
        txtSearch.multiline = False
        txtSearch.on_text_validate = self.on_search_validate

        self.widgets = dict()
        self.widgets["txtSearch"] = txtSearch
        self.add_widget(txtSearch)

    def on_search_validate(self):
        txtSearch = self.widgets["txtSearch"]
        print(f"input: {txtSearch.text}")
