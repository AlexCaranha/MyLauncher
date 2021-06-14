
from kivymd.uix.list import MDList
from kivy.uix.scrollview import ScrollView

def create_scroll_list_items(list_items):
    scroll = ScrollView()
    md_list = MDList()

    for item in list_items:       
        md_list.add_widget(item)

    scroll.add_widget(md_list)
    return scroll