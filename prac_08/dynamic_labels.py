"""
Prac 08 - Dynamic Labels
CP1404
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty
from random import random


class DynamicLabels(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Build the labels dynamically from a list of names"""
        for name in self.names:
            # create a button for each data entry, specifying the text
            temp_label = Label(text=name)
            # set the label's text colour to a random colour. Just for fun.
            temp_label.color = (random(), random(), random(), 1)
            # set the label's font size
            temp_label.font_size = 30
            # add the label to the "main" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabels().run()
