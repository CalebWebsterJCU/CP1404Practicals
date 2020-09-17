"""
Convert Temperature
17/09/2020
This Kivy Program Converts celsius to fahrenheit and fahrenheit to celsius.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window


class ConvertTemperature(App):
    """Create GUI Program."""
    temp_output_text = StringProperty()
    mode_text = StringProperty()
    C_TO_F_MODE = "c-f"
    F_TO_C_MODE = "f-c"

    def __init__(self, **kwargs):
        """Initialize class."""
        super().__init__(**kwargs)
        self.mode = self.F_TO_C_MODE

    def build(self):
        """Create GUI."""
        self.root = Builder.load_file("convert_temperature.kv")
        self.temp_output_text = "Enter Temperature"
        self.mode_text = "Fahrenheit to Celsius"
        return self.root

    def handle_convert(self):
        """Convert fahrenheit to celsius or celsius to fahrenheit, depending on which mode the program is in."""
        temp_to_convert = self.get_valid_temperature()
        if self.mode == self.F_TO_C_MODE:  # Fahrenheit to celsius
            self.temp_output_text = str(round((temp_to_convert - 32) * (5 / 9), 4))
        else:  # celsius to fahrenheit
            self.temp_output_text = str(round(temp_to_convert * (9 / 5) + 32))

    def get_valid_temperature(self):
        """Get temperature, returning zero if it is invalid."""
        try:
            temperature = float(self.root.ids.temp_input.text)
            return temperature
        except ValueError:
            return 0

    def change_mode(self):
        """Change program mode (celsius to fahrenheit or fahrenheit to celsius)."""
        if self.mode == self.F_TO_C_MODE:
            self.mode = self.C_TO_F_MODE
            self.mode_text = "Celsius to Fahrenheit"
        else:
            self.mode = self.F_TO_C_MODE
            self.mode_text = "Fahrenheit to Celsius"


if __name__ == '__main__':
    ConvertTemperature().run()
