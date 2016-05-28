from .colors import _process_color
from . import graphics
from . import svg

class Canvas:

    def __init__(self, width, height, background_color=None):
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

        self.graphics = []


    def __repr__(self):
        return "<Canvas %i×%i (%i Graphics)>" % (
         self.width, self.height, len(self.graphics)
        )


    def add_rectangle(self, *args, **kwargs):
        self.graphics.append(graphics.Rectangle(*args, **kwargs))


    def add_line(self, *args, **kwargs):
        self.graphics.append(graphics.Line(*args, **kwargs))


    def add_polygon(self, *args, **kwargs):
        self.graphics.append(graphics.Polygon(*args, **kwargs))


    def add_text(self, *args, **kwargs):
        self.graphics.append(graphics.Text(*args, **kwargs))


    def save(self, path):
        with open(path, "w") as f:
            f.write(self.to_svg())


    to_svg = svg.generate_canvas_svg
