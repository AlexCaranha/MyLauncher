
from kivy.logger import COLORS
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.list import TwoLineListItem

from kivy.uix.scrollview import ScrollView
from pages.search_util import search
from util import open_file, get_file_name

class SearchScreen(Screen):
    def build(self):
        self.name = "SearchPage"

        self.layout = MDBoxLayout()
        self.layout.orientation = 'vertical'

        self.setup_search_bar(self.layout)
        self.setup_results(self.layout)
        self.search_sentence("firefox*.exe")

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
        # self.txtSearch.keyboard_on_key_down = self.44
        self.txtSearch.on_text_validate = self.on_search_validate
        
        self.layout_bar.add_widget(self.txtSearch)
        main_layout.add_widget(self.layout_bar)

    def setup_results(self, main_layout):
        self.scroll = ScrollView()
        self.results = MDList()

        self.scroll.add_widget(self.results)
        main_layout.add_widget(self.scroll)

    # def keyboard_on_key_down(self, window, keycode, text, modifiers):
    #     if keycode is not None and len(keycode) == 2 and keycode[1] == "tab":
    #         self.set_select_item(0)
    #         self.scroll.focus = True

    def on_search_validate(self):
        sentence = self.txtSearch.text
        self.search_sentence(sentence)

    def search_sentence(self, sentence):
        results = search(sentence, None, 50)

        self.results.clear_widgets()
        
        for file_path in results:
            file_name = get_file_name(file_path)
            item = TwoLineListItem(text=file_name, secondary_text=file_path, on_press=self.on_press_result)                        
            self.results.add_widget(item)

    # def what_component_has_focus(self):
    #     item = self.txtSearch.focus_next
    #     print(item)

    # def set_select_index(self, index):
    #     self.selected = index

    # def set_select_item(self, index):
    #     self.select_index = index

    #     for item in self.results.children:
    #         item.bg_color = (0, 0, 0, 0)

    #     qtd = len(self.results.children)

    #     if 0 <= index < qtd:
    #         item = self.results.children[qtd-1-index]
    #         item.bg_color = (75/255, 152/255, 196/255, 1)
    #         self.scroll.update_from_scroll


    def on_press_result(self, sender):
        open_file(sender.text)
