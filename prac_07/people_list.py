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
        for name in self.names_to_ages:
            self.create_button(name)
        return self.root

    def create_button(self, name):
        """Create a button with a name."""
        button = Button(text=name, id=name)
        button.bind(on_press=self.display_person_info)
        self.root.ids.names_box.add_widget(button)

    def display_person_info(self, instance):
        """Display person's name and age in label."""
        name = instance.id
        self.root.ids.info_display.color = (1, 1, 1, 1)
        self.person_info = "{}, age {}".format(name, self.names_to_ages.get(name))

    def add_person(self):
        """Create a button widget with the name and age entered, if they are valid. Also add the person to dictionary and file."""
        age = 0
        name_is_valid = False
        age_is_valid = False
        name = self.root.ids.name_input.text
        if name != "":
            name_is_valid = True
        try:
            age = int(self.root.ids.age_input.text)
            if age >= 0:
                age_is_valid = True
        except ValueError:
            pass
        if name_is_valid and age_is_valid:
            self.create_button(name)
            self.root.ids.info_display.color = (1, 1, 1, 1)
            self.person_info = "{}, age {} added!".format(name, age)
            self.names_to_ages[name] = age
            file_out = open(FILE_NAME, 'a')
            print("{}: {}".format(name, age), file=file_out)
            file_out.close()
        else:
            self.root.ids.info_display.color = (1, 0, 0, 1)
            self.person_info = "Invalid name or age"


if __name__ == '__main__':
    PeopleList().run()
