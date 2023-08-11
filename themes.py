from elements.styles_and_themes.theme import *

night_background = Background(Color((60, 60, 60)))

night_theme = Theme(
    background=night_background,
    buttons=Style((255, 255, 255), (40, 40, 40), 40),
    text=Style((255, 255, 255), None, 0),
    error_text=Style((255, 0, 0), None, 0),
    contacts=Style((255, 255, 255), (40, 40, 40), 40),
    find_contacts=Style((255, 255, 255), (40, 40, 40), 40)
)

day_background = Background(Color((255, 255, 255)))

day_theme = Theme(
    background=day_background,
    buttons=Style((0, 0, 0), (240, 240, 240), 40),
    text=Style((0, 0, 0), None, 0),
    error_text=Style((255, 0, 0), None, 0),
    contacts=Style((0, 0, 0), (240, 240, 240), 40),
    find_contacts=Style((0, 0, 0), (240, 240, 240), 40)
)
