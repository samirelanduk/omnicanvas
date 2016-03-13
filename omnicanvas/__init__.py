from . import graphics
from . import svg

class Canvas:

    def __init__(self, width, height, background_color="#FFFFFF"):
        self._width = int(width)
        self._height = int(height)

        self.background_color = background_color

        self.graphics = []


    def __repr__(self):
        return "<%i × %i canvas object with %i graphics>" % (
         self._width,
         self._height,
         len(self.graphics)
        )


    def width(self):
        return self._width


    def height(self):
        return self._height


    def resize(self, width, height):
        for graphic in self.graphics:
            graphic.scale(width / self._width, height / self._height)
        self._width = width
        self._height = height


    def draw_line(self, *args, **kwargs):
        self.graphics.append(graphics.Line(*args, **kwargs))
        return self.graphics[-1]


    def draw_path(self, *args, **kwargs):
        self.graphics.append(graphics.Path(*args, **kwargs))
        return self.graphics[-1]


    def draw_rectangle(self, *args, **kwargs):
        self.graphics.append(graphics.Rectangle(*args, **kwargs))
        return self.graphics[-1]


    def draw_polygon(self, *args, **kwargs):
        self.graphics.append(graphics.Rectangle(*args, **kwargs))
        return self.graphics[-1]


    def draw_oval(self, *args, **kwargs):
        self.graphics.append(graphics.Oval(*args, **kwargs))
        return self.graphics[-1]


    def draw_arc(self, *args, **kwargs):
        self.graphics.append(graphics.Arc(*args, **kwargs))
        return self.graphics[-1]


    def draw_text(self, *args, **kwargs):
        self.graphics.append(graphics.Text(*args, **kwargs))
        return self.graphics[-1]


    def draw_text_boundary(self, *args, width, height, max_font_size=None, **kwargs):
        font_size = height
        if max_font_size and font_size > max_font_size:
            font_size = max_font_size
        self.draw_text(*args, font_size=font_size, **kwargs)
        return self.graphics[-1]


    def render(self, file_type):
        if file_type.lower() == "svg":
            return svg.canvas_to_svg(self)


    def save(self, file_type, file_name):
        file_contents = self.render(file_type=file_type)
        with open(file_name, "w") as f:
            f.write(file_contents)
