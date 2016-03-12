class GenericBox:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height



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
    pass



class Arc(GenericBox, GenericShape):
    pass



class Text(GenericBox):
    pass
