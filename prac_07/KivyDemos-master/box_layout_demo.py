"""
Box Layout Demo
16/09/2020
This GUI program takes a name input and prints a greeting.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import random as r


class BoxLayoutDemo(App):
    """Kivy app that prints greetings."""
    FILE_NAME = "greetings.txt"

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.greetings = self.read_greetings()

    def build(self):
        """Build the GUI."""
        Window.size = (750, 300)
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def read_greetings(self):
        """Read list of random greetings from a file."""
        greetings = []
        file_in = open(self.FILE_NAME, 'r')
        for line in file_in:
            greetings.append(line.strip())
        file_in.close()
        return greetings

    def handle_greet(self):
        """Get name input and print greeting with that name."""
        # print('Hi')
        random_greeting = r.choice(self.greetings)
        random_greeting = random_greeting.replace("[name]", self.root.ids.input_name.text)
        # self.root.ids.output_label.text = "Hello {}!".format(self.root.ids.input_name.text)
        self.root.ids.output_label.text = random_greeting

    def clear_fields(self):
        """Clear input and output fields."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
