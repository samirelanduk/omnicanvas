from .colors import _process_color
from . import graphics

class Canvas:

    def __init__(self, width, height, background_color=None, border_width=0,
     border_style="-", border_color="#000000"):
        if isinstance(width, float):
            width = round(width)
        if not isinstance(width, int):
            raise TypeError("Width must be numeric, not '%s'" % width)
        self.width = width

        if isinstance(height, float):
            height = round(height)
        if not isinstance(height, int):
            raise TypeError("Height must be numeric, not '%s'" % height)
        self.height = height

        if background_color is None:
            self.background_color = None
        else:
            self.background_color = _process_color(background_color)

        if not isinstance(border_width, int) and not isinstance(border_width, float):
            raise TypeError("Border width must be numeric, not '%s'" % border_width)
        self.border_width = border_width

        if not isinstance(border_style, str):
            raise TypeError("Border style must be str, not '%s'" % border_style)
        if border_style not in ("-", "--", ".."):
            raise ValueError("'%s' is not a valid line style" % border_style)
        self.border_style = border_style

        self.border_color = _process_color(border_color)

        self.graphics = []


    def __repr__(self):
        return "<Canvas %i×%i (%i Graphics)>" % (
         self.width, self.height, len(self.graphics)
        )


    def add_rectangle(self, *args, **kwargs):
        self.graphics.append(graphics.Rectangle(*args, **kwargs))
