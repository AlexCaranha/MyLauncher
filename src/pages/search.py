import os

from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.list import OneLineListItem

from kivy.uix.scrollview import ScrollView
from pages.search_util import search

class SearchScreen(Screen):
    def build(self):
        self.name = "SearchPage"

        self.layout = MDBoxLayout()
        self.layout.orientation = 'vertical'
        # self.layout.spacing = dp(5)
        # self.layout.padding = dp(70)

        self.setup_search_bar(self.layout)
        self.setup_results(self.layout)
        # self.setup_recycle_view_data()

        self.add_widget(self.layout)

    def setup_search_bar(self, main_layout):
        self.layout_bar = MDBoxLayout()
        self.layout_bar.spacing = dp(10)
        self.layout_bar.padding = dp(20)
        self.layout_bar.adaptive_height = True

        self.txtSearch = MDTextField()
        self.txtSearch.name = "txtSearch"
        self.txtSearch.hint_text = "How can I help you?"
        self.txtSearch.mode = "rectangle"
        self.txtSearch.focus = True
        self.txtSearch.multiline = False
        self.txtSearch.on_text_validate = self.on_search_validate
        
        self.layout_bar.add_widget(self.txtSearch)
        main_layout.add_widget(self.layout_bar)

    def setup_results(self, main_layout):
        self.scroll = ScrollView()
        self.results = MDList()

        self.scroll.add_widget(self.results)
        main_layout.add_widget(self.scroll)
        
    def on_search_validate(self):
        sentence = self.txtSearch.text

        print(f"input: {sentence}")        
        results = search(sentence, ".exe")

        self.results.clear_widgets()
        for filename, modified_on in results:
            item= OneLineListItem(text=filename, on_press=self.on_press_result)
            self.results.add_widget(item)

    def on_press_result(self, sender):
        os.startfile(sender.text)
