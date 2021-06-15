
from kivymd.uix.list import MDList
from kivy.uix.scrollview import ScrollView

def create_scroll_list_items(list_items):
    scroll = ScrollView()
    md_list = MDList()

    for item in list_items:       
        md_list.add_widget(item)

    scroll.add_widget(md_list)
    return scroll

def add_list_items_in_scroll(list_items, scroll):
    md_list = MDList()

    for item in list_items:       
        md_list.add_widget(item)

    scroll.add_widget(md_list)

def get_component_by_name(name, object):
    if object == None or object.children == None:
        return None

    if hasattr(object, 'name') and name == object.name:
        return object

    for child in object.children:
       found = get_component_by_name(name, child) 

       if found != None:
           return found

    return None

def get_component_by_id(id, object):
    if object == None or object.children == None:
        return None

    if hasattr(object, 'ids') and id in object.ids:
        return object.ids[id]

    for child in object.children:
       found = get_component_by_id(id, child) 

       if found != None:
           return found

    return None