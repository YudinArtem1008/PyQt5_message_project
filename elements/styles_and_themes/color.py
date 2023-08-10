from functions import rgb


class Color:
    def __init__(self, color):
        if type(color) == tuple and len(color) == 2:
            self.color = color[0]
        if type(color) == tuple and len(color) == 3:
            self.color = rgb(color[0], color[1], color[2])[0]

    def get_color(self):
        return self.color
