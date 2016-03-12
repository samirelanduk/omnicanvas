class GenericBox:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def center(self):
        return (self.x + self.width / 2, self.y + self.height / 2)



class GenericLine:

    def __init__(self, line_style="-", line_width=1, line_color="#000000"):
        self.line_style = line_style
        self.line_width = line_width
        self.line_color = line_color



class GenericShape(GenericLine):

    def __init__(self, fill_color=None, opacity=1, **kwargs):
        self.fill_color = fill_color
        self.opacity = opacity
        GenericLine.__init__(self, **kwargs)



class Line(GenericLine):

    def __init__(self, x1, y1, x2, y2, **kwargs):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        GenericLine.__init__(self, **kwargs)


    def __repr__(self):
        return "<Line object: (%i,%i) to (%i,%i)>" % (
         self.x1, self.y1, self.x2, self.y2
        )



class Path(GenericLine):

    def __init__(self, *points, **kwargs):
        assert len(points) % 2 == 0, "An even number of points must be supplied"
        self.points = list(zip(points[::2], points[1::2]))
        GenericLine.__init__(self, **kwargs)


    def __repr__(self):
        return "<Path object: %s points>" % len(self.points)



class Rectangle(GenericBox, GenericShape):

    def __init__(self, *args, **kwargs):
        GenericBox.__init__(self, *args)
        GenericShape.__init__(self, **kwargs)


    def __repr__(self):
        return "<%i × %i Rectangle object at (%i,%i)>" % (
         self.width, self.height, self.x, self.y
        )



class Polygon(GenericShape):

    def __init__(self, *points, **kwargs):
        assert len(points) % 2 == 0, "An even number of points must be supplied"
        self.points = list(zip(points[::2], points[1::2]))
        GenericShape.__init__(self, **kwargs)


    def __repr__(self):
        return "<Polygon object: %s vertices>" % len(self.points)



class Oval(GenericBox, GenericShape):

    def __init__(self, *args, **kwargs):
        GenericBox.__init__(self, *args)
        GenericShape.__init__(self, **kwargs)


    def __repr__(self):
        return "<%i × %i Oval object centered at %s>" % (
         self.width, self.height, str(self.center()).replace(" ", "")
        )



class Arc(GenericBox, GenericShape):

    def __init__(self, *args, start_angle, end_angle, connect=None, **kwargs):
        assert start_angle <= 360, "Start angle %i greater than 360" % start_angle
        assert end_angle <= 360, "End angle %i greater than 360" % end_angle

        self.start_angle = start_angle
        self.end_angle = end_angle
        self.connect = connect if connect == "pie" or connect == "direct" else None
        GenericBox.__init__(self, *args)
        GenericShape.__init__(self, **kwargs)


    def __repr__(self):
        return "<%i × %i %s Arc object at (%i,%i)>" % (
         self.width, self.height,
         "Unclosed" if not self.connect else self.connect,
         self.x, self.y
        )


    def angle(self):
        if self.end_angle >= self.start_angle:
            return self.end_angle - self.start_angle
        else:
            return self.end_angle + (360 - self.start_angle)



class Text:

    def __init__(self, x, y, text, font_family="Tahoma", font_size=24,
     vertical_align="center", horizontal_align="center"):
        self.x = x
        self.y = y
        self.text = str(text)
        self.font_family = font_family
        self.font_size = font_size
        self.vertical_align = vertical_align
        self.horizontal_align = horizontal_align


    def __repr__(self):
        return '<"%s" Text object at (%i,%i)>' % (self.text, self.x, self.y)
