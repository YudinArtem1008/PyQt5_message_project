from exceptions import ColorException


def rgb(r, g, b):
    if not 0 <= r <= 255 or not 0 <= g <= 255 or not 0 <= b <= 255:
        raise ColorException("Incorrect value for color")
    return tuple(["#{:02x}{:02x}{:02x}".format(r, g, b), 1])
