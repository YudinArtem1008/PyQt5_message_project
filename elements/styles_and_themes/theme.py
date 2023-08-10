from .elements import *
from .color import Color


class Style:
    def __init__(self, main_color, background_color, d_color):
        self.main_color = Color(main_color)
        if background_color is None:
            self.background_color = None
        else:
            self.background_color = Color(background_color)
        self.d_color = d_color


class Theme:
    def __init__(self, data=None, **styles):
        if data is not None:
            self.data = data
            return

        class DataKeeper:
            def __init__(self, styles):
                self.styles = styles

            def __getitem__(self, item):
                return self.styles[item]

        self.data = DataKeeper(styles)
        self.data.styles = styles
