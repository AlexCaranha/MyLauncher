
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
from util import open_file, get_file_name, is_not_blank

class SearchScreen(Screen):
    def build(self):
        self.name = "SearchPage"

        self.layout = MDBoxLayout()
        self.layout.orientation = 'vertical'

        self.setup_search_bar(self.layout)
        self.setup_results(self.layout)
        self.setup_variables()

        self.set_selected_item(None)
        self.search_sentence(None)

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
        # self.txtSearch.keyboard_on_key_down = self.keyboard_on_key_down_wrapper
        # self.txtSearch.on_text_validate = self.on_enter
        
        self.layout_bar.add_widget(self.txtSearch)
        main_layout.add_widget(self.layout_bar)

    # def on_enter(instance, value):
    #     print(f"User pressed enter in {instance}: {value}")

    def setup_results(self, main_layout):
        self.scroll = ScrollView()
        self.results = MDList()

        self.scroll.add_widget(self.results)
        main_layout.add_widget(self.scroll)

    def get_selected_item(self):
        return (self.item_selected_index, self.item_selected)            

    def set_selected_item(self, item):
        index_selected, item_selected = self.get_result_by_item(item)
        self.item_selected_index = index_selected
        self.item_selected = item_selected

    def set_selected_item_by_variation(self, variation):
        if variation == None:
            self.item_selected = None
            self.item_selected_index = -1
            self.refresh_items_colors()

            print(f"index selected: {self.item_selected_index}.")
            return

        new_index = self.item_selected_index + variation
        qtd_results = self.get_qtd(self.results)

        if new_index < 0:
            new_index = qtd_results - 1

        if new_index >= qtd_results:
            new_index = 0

        # indexes               
        self.item_selected_index = new_index
        self.item_selected = self.get_result_by_index(new_index)

        # colors
        self.refresh_items_colors()

        print(f"index selected: {self.item_selected_index}.")


    def refresh_items_colors(self):
        for item in self.results.children:
            self.set_background_color(item, self.unselected_color)  

        self.set_background_color(self.item_selected, self.selected_color)

    def set_background_color(self, item, color):
        if item == None or color == None:
            return

        item.bg_color = color

    def get_qtd(self, lista:MDList):
        return 0 if lista == None else len(lista.children)

    def get_result_by_index(self, index:int):
        return self.results.children[index]

    def get_result_by_item(self, item_selected):
        for index, item in enumerate(self.results.children):
            if item == item_selected:
                return (index, item)

        return (-1, None)

    # def keyboard_on_key_down_wrapper(self, window, keycode, text, modifiers):
    #     if keycode[1] == "enter":
    #         self.set_selected_item_by_variation(None)
    #         self.refresh_items_colors()
    #         self.search_sentence(self.txtSearch.text)
    #         pass

    #     if keycode[1] == "backspace":
    #         self.txtSearch.text = self.txtSearch.text[:-1] if len(self.txtSearch.text) > 0 else self.txtSearch.text

    #     if keycode[1] == "up":
    #         self.set_selected_item_by_variation(+1)

    #     if keycode[1] == "down":
    #         self.set_selected_item_by_variation(-1)

        # print(f"keycode = {keycode}")

    def search_sentence(self, sentence):
        self.results.clear_widgets()
        
        lista = [
            ("vinci (vnc)", "Scripts para aumentar a produtividade"),
            ("snippets (snip)", "Scrips utilitários.")]

        for item_result in lista:
            primary_text = item_result[0]
            segundary_text = item_result[1]

            if is_not_blank(sentence) and not (sentence in primary_text or sentence in segundary_text):
                continue

            item = TwoLineListItem(text=primary_text, secondary_text=segundary_text, on_press=self.on_press_result)
            item.bg_color = self.unselected_color
            item.on_release = self.focus_on_txtSearch

            self.results.add_widget(item)
        
        self.txtSearch.focus = True

    def on_press_result(self, sender):
        self.set_selected_item(sender)
        self.refresh_items_colors()

        print(f"{sender.text} clicked.")
        self.txtSearch.focus = True

    def focus_on_txtSearch(self):
        self.txtSearch.focus = True
