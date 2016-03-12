from . import graphics

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


    def draw_line(self, *args, **kwargs):
        self.graphics.append(graphics.Line(*args, **kwargs))


    def draw_path(self, *args, **kwargs):
        self.graphics.append(graphics.Path(*args, **kwargs))


    def draw_rectangle(self, *args, **kwargs):
        self.graphics.append(graphics.Rectangle(*args, **kwargs))


    def draw_polygon(self, *args, **kwargs):
        self.graphics.append(graphics.Rectangle(*args, **kwargs))


    def draw_oval(self, *args, **kwargs):
        self.graphics.append(graphics.Oval(*args, **kwargs))


    def draw_arc(self, *args, **kwargs):
        self.graphics.append(graphics.Arc(*args, **kwargs))


    def draw_text(self, *args, **kwargs):
        self.graphics.append(graphics.Text(*args, **kwargs))


    def draw_text_boundary(self, x, y, width, height, text, max_font_size=None,
     font_family="Tahoma", vertical_align="center", horizontal_align="center"):
        self.graphics.append(None) # To add later
