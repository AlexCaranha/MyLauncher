from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

class Example(MDApp):
    def build(self):
        self.layout = MDBoxLayout()
        self.layout.orientation = 'vertical'
        
        self.setup_search_bar(self.layout)
        self.setup_results(self.layout)

        screen = MDScreen()
        screen.add_widget(self.layout)
        return screen

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
        # self.txtSearch.on_text_validate = self.on_search_validate
        
        self.layout_bar.add_widget(self.txtSearch)
        main_layout.add_widget(self.layout_bar)

    def setup_results(self, main_layout):
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=False,
            column_data=[
                ("No.", dp(30)),
                ("Status", dp(30)),
                ("Stage", dp(100)),
            ],
            row_data=[
                (
                    "1",
                    (
                        "alert",
                        [255 / 256, 165 / 256, 0, 1],
                        "No Signal"
                    ),
                    "Astrid: NE shared managed",
                ),
                (
                    "5",
                    (
                        "checkbox-marked-circle",
                        [39 / 256, 174 / 256, 96 / 256, 1],
                        "Online",
                    ),
                    "Sirius: prod independent account",
                ),
            ],
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        main_layout.add_widget(self.data_tables)

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)

    def sort_on_signal(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    def sort_on_schedule(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [
                        int(l[1][-2].split(":")[0]) * 60,
                        int(l[1][-2].split(":")[1]),
                    ]
                ),
            )
        )

    def sort_on_team(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))


Example().run()