from .elements import *


class Style:
    def __init__(self, background: Background, background_contacts, background_elements, background_message=None):
        self.background = background
        self.background_contacts = background_contacts
        self.background_elements = background_elements


class Theme:
    def __init__(self, theme='day'):
        self.theme = theme

    def get_css(self):
        if self.theme == 'day':
            return open('styles/light_elements.css', 'r').read()
        else:
            return open('styles/dark_elements.css', 'r').read()

    def change_theme(self):
        if self.theme == 'day':
            self.theme = 'night'
        else:
            self.theme = 'day'
