"""
Dynamic Labels
16/09/2020
This GUI Program displays each name in a list of names as a different label.
The Comments are only to help me remember whats going on.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """Kivy program to display names as different widgets."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Donald", "Huey", "Deuy", "leuy", "Scrooge", "Daisy"]

    def build(self):
        """Construct the GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            name_label = Label(text=name)  # create a label with the name text
            self.root.ids.names_box.add_widget(name_label)  # add the label to names_box
        return self.root

    def create_name_label(self):
        """Create a label with the entered name."""
        name = self.root.ids.name_input.text  # get text from name_input box
        self.root.ids.names_box.add_widget(Label(text=name))  # create a label with the name text and add it to names_box
        self.root.ids.name_input.text = ""  # clear all text from name_input box


if __name__ == '__main__':
    DynamicLabels().run()
