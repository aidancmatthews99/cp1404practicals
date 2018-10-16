from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        Window.size = (300, 100)
        self.root = Builder.load_file('convert_miles_to_kilometres.kv')
        return self.root

    def handle_convert(self, miles):
        try:
            self.root.ids.output_label.text = str(float(miles) * MILES_TO_KM)
        except ValueError:
            self.root.ids.output_label.text = '0.0'

    def handle_increment(self, change, initial):
        try:
            final_value = str(float(initial) + change)
            self.root.ids.input_label.text = final_value
        except ValueError:
            self.root.ids.input_label.text = '0.0'
            final_value = '0.0'
        self.handle_convert(final_value)


BoxLayoutDemo().run()
