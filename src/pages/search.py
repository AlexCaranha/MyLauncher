
from typing import KeysView
from kivy.logger import COLORS, GREEN
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.list import TwoLineListItem
from kivy.utils import get_color_from_hex, hex_colormap

from kivy.uix.scrollview import ScrollView
from util import open_file, get_file_name

class SearchScreen(Screen):
    def build(self):
        self.name = "SearchPage"

        self.layout = MDBoxLayout()
        self.layout.orientation = 'vertical'

        self.setup_search_bar(self.layout)
        self.setup_results(self.layout)
        self.setup_variables()

        self.set_selected_item(None)
        self.search_sentence("start")        

        self.add_widget(self.layout)

    def get_color(self, color_name: str):
        hex_value = hex_colormap[color_name] if color_name in hex_colormap else None

        if hex_value == None:
            return None

        output = get_color_from_hex(hex_value)
        return output

    def setup_variables(self):
        self.selected_color = self.get_color("lightsteelblue")
        self.unselected_color = get_color_from_hex("#eeeeee")

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
        self.txtSearch.keyboard_on_key_down = self.keyboard_on_key_down_wrapper
        # self.txtSearch.on_text_validate = self.on_search_validate
        
        self.layout_bar.add_widget(self.txtSearch)
        main_layout.add_widget(self.layout_bar)

    def setup_results(self, main_layout):
        self.scroll = ScrollView()
        self.results = MDList()

        self.scroll.add_widget(self.results)
        main_layout.add_widget(self.scroll)

    def get_selected_item(self):
        return (self.item_selected_index, self.item_selected)            

    def set_selected_item(self, variation):
        if variation == None:
            self.item_selected_old = None
            self.item_selected_index_old = -1

            self.item_selected = None
            self.item_selected_index = -1
            return

        new_index = self.item_selected_index + variation
        qtd_results = self.get_qtd(self.results)

        if new_index < 0:
            new_index = qtd_results - 1

        if new_index >= qtd_results:
            new_index = 0

        # indexes
        self.item_selected_old = self.item_selected
        self.item_selected_index_old = self.item_selected_index
        
        self.item_selected_index = new_index
        self.item_selected = self.get_result(new_index)

        # colors
        self.refresh_items_colors()

        print(f"index selected: {self.item_selected_index}")


    def refresh_items_colors(self):
        self.set_background_color(self.item_selected_old, self.unselected_color)
        self.set_background_color(self.item_selected, self.selected_color)

    def set_background_color(self, item, color):
        if item == None:
            return

        item.bg_color = color

    def get_qtd(self, lista:MDList):
        return 0 if lista == None else len(lista.children)

    def get_result(self, index:int):
        return self.results.children[index]

    def keyboard_on_key_down_wrapper(self, window, keycode, text, modifiers):
        if keycode[1] == "enter":
            self.selected_color = self.get_color(self.txtSearch.text)
            self.refresh_items_colors()
            pass

        if keycode[1] == "backspace":
            self.txtSearch.text = self.txtSearch.text[:-1] if len(self.txtSearch.text) > 0 else self.txtSearch.text

        if keycode[1] == "up":
            self.set_selected_item(+1)

        if keycode[1] == "down":
            self.set_selected_item(-1)

        print(f"keycode = {keycode}")

    def search_sentence(self, sentence):
        self.results.clear_widgets()
        
        results = [
            ("Vinci", "Scripts para aumentar a produtividade"),
            ("Alpha Tools", "Scripts para facilitar a obtenção de cadastros."),
            ("Util", "Scrips utilitários.")]

        for result in results:
            primary_text = result[0]
            segundary_text = result[1]
            item = TwoLineListItem(text=primary_text, secondary_text=segundary_text, on_press=self.on_press_result)
            item.bg_color = self.unselected_color

            self.results.add_widget(item)


    # def search_sentence(self, sentence):
    #     results = search(sentence, None, 50)

    #     self.results.clear_widgets()
        
    #     for file_path in results:
    #         file_name = get_file_name(file_path)
    #         item = TwoLineListItem(text=file_name, secondary_text=file_path, on_press=self.on_press_result)                        
    #         self.results.add_widget(item)

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
