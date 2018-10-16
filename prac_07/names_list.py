
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class NamesList(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Steve Irwin', "Fred Flintstone", 'George Jetson']

    def build(self):
        self.title = 'Names List'
        self.root = Builder.load_file('names_list.kv')
        self.add_names()
        return self.root

    def add_names(self):
        for name in self.names:
            label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(label)


NamesList().run()