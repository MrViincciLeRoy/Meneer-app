from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ListProperty

class TitleLabel(Label):
    """A custom label for screen titles with a larger font size."""
    def __init__(self, **kwargs):
        super(TitleLabel, self).__init__(**kwargs)
        self.font_size = '24sp'
        self.bold = True

class ActionButton(Button):
    """A custom button with a default background color."""
    background_color = ListProperty([0.2, 0.6, 0.8, 1]) # A nice blue
    def __init__(self, **kwargs):
        super(ActionButton, self).__init__(**kwargs)
        self.background_normal = '' # Allows background_color to work
        self.background_color = self.background_color
