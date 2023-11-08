"""
Prac 08 - Convert Miles to KM
CP1404
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM_CONSTANT = 1.609


class ConvertMilesKm(App):
    """The class variable in the app is the 'model'."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = ""
        return self.root

    def handle_conversion(self, value):
        """Converts miles to kilometres when an event occurs, likely a button press"""
        try:
            miles = float(value)
            kilometres = miles * MILES_TO_KM_CONSTANT
            self.message = str(kilometres)
        except ValueError:
            self.message = "0.0"

    def handle_increment(self, current_value, increment):
        """Updates and increments the text of the input field"""
        try:
            self.root.ids.input_text.text = str(float(current_value) + float(increment))
        except ValueError:
            self.root.ids.input_text.text = increment


# create and start the App running
ConvertMilesKm().run()
