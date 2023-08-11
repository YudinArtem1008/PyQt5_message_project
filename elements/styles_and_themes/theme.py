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
        self.add_to_css()

    def add_to_css(self):
        classes = {'background': 'QMainWindow',
                   'buttons': 'QPushButton',
                   'text': 'QLabel',
                   'error_text': 'QLabel#label',
                   'contacts': 'QListWidget',
                   'find_contacts': 'QLineEdit'}
        qss = ""
        for des, style in self.data.styles.items():
            qss += f'{classes[des]}'
            qss += ' {\n'
            if style.background_color is not None:
                qss += f'    background-color: {style.background_color.get_color()};\n'
            if type(style) == Style:
                qss += f'    color: {style.main_color.get_color()};\n'
            if des == 'find_contacts':
                qss += """    border-radius: 15px;
    border: 2px solid rgb(55, 55, 55);
    padding-left: 10px;
    padding-right: 10px;\n"""
            qss += '}\n'
        with open('elements/styles/elements.css', 'w') as f:
            f.write(qss)
            f.close()
