"""
Convert Miles to KM
16/09/2020
This Kivy Program Converts Miles to Kilometers.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKm(App):
    """ConvertMilesKm is an app that converts miles to km."""

    MILES_TO_KM = 1.60934

    def build(self):
        """Build the Kivy app from the kv file."""
        self.root = Builder.load_file("convert_miles_km.kv")
        Window.size = (500, 200)
        # self.km_output = "Yes"
        return self.root

    def handle_convert(self):
        """Convert miles to km."""
        miles = self.get_valid_miles()
        km = round(miles * self.MILES_TO_KM, 2)
        self.root.ids.km_output.text = str(km)

    def handle_increment(self, amount):
        """Increment input by a certain amount."""
        miles_input = self.get_valid_miles()
        self.root.ids.miles_input.text = str(miles_input + amount)

    def get_valid_miles(self):
        """Get miles input, returning 0 if it is invalid."""
        try:
            miles_input = float(self.root.ids.miles_input.text)
        except ValueError:
            miles_input = 0
        return miles_input


if __name__ == '__main__':
    ConvertMilesKm().run()
