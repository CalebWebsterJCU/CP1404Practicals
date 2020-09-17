"""
People List
17/09/2020
This Kivy program reads people's names and ages from a file and displays each person as a separate button in the GUI.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.button import Button

FILE_NAME = "people_list.txt"


def create_dict_from_file(file_name):
    """Read entries (separated by ": ") from a file and return a dictionary."""
    the_dict = {}
    file_in = open(file_name, 'r')
    for line in file_in:
        parts = line.strip().split(": ")
        the_dict[parts[0]] = int(parts[1])
    file_in.close()
    return the_dict


class PeopleList(App):
    """People list app."""
    person_info = StringProperty()

    def __init__(self, **kwargs):
        """Initialize People list app."""
        super().__init__(**kwargs)
        self.names_to_ages = create_dict_from_file(FILE_NAME)

    def build(self):
        """Build GUI."""
        self.title = "People List"
        self.root = Builder.load_file("people_list.kv")
        self.create_buttons()
        return self.root

    def create_buttons(self):
        """Create a button with a name for each entry in dictionary."""
        for name in self.names_to_ages:
            button = Button(text=name, id=name)
            button.bind(on_press=self.display_person_info)
            self.root.ids.names_box.add_widget(button)

    def display_person_info(self, instance):
        """Display person's name and age in label."""
        name = instance.id
        self.person_info = "{}, age {}".format(name, self.names_to_ages.get(name))


if __name__ == '__main__':
    PeopleList().run()
