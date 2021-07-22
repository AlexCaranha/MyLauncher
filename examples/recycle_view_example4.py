from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.metrics import dp

class RV(RecycleView):
    def setup(self):
        self.recycle_box_layout = RecycleBoxLayout()
        self.recycle_box_layout.default_size = None, dp(56)
        self.recycle_box_layout.default_size_hint = 1, None
        self.recycle_box_layout.size_hint_y = None
        # self.recycle_box_layout.height = self.minimum_height
        self.recycle_box_layout.orientation = 'vertical'

        self.add_widget(self.recycle_box_layout)


class TestApp(App):
    def build(self):
        rv = RV()
        rv.setup()
        rv.viewclass = 'Label'
        rv.data = [{'text': str(x)} for x in range(10)]
        return rv

if __name__ == '__main__':
    TestApp().run()