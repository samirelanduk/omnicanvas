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


    def draw_line(self, x1, y1, x2, y2, line_width=1, line_color="#000000",
     line_style="-"):
        pass


    def draw_path(self, *points, line_width=1, line_color="#000000",
     line_style="-"):
        pass


    def draw_rectangle(self, x, y, width, height, line_width=1,
     line_color="#000000", line_style="-", fill_color=None, opacity=1):
        pass


    def draw_polygon(self, *points, line_width=1,
     line_color="#000000", line_style="-", fill_color=None, opacity=1):
        pass


    def draw_oval(self, x, y, width, height, line_width=1,
     line_color="#000000", line_style="-", fill_color=None, opacity=1):
        pass


    def draw_arc(self, x, y, width, height, start_angle, end_angle,
     connect=None, line_width=1, line_color="#000000", line_style="-",
      fill_color=None, opacity=1):
        pass


    def draw_text(self, x, y, text, font_family="Tahoma", font_size=24,
     vertical_align="center", horizontal_align="center"):
        pass


    def draw_text_boundary(self, x, y, width, height, text, max_font_size=None,
     font_family="Tahoma", vertical_align="center", horizontal_align="center"):
        pass
