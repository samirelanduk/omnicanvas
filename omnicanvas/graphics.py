class GenericBox:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height



class GenericLine:

    def __init__(self, line_style, line_width, line_color):
        self.line_style = line_style
        self.line_width = line_width
        self.line_color = line_color



class GenericShape:

    def __init__(self, fill_color, opacity):
        self.fill_color = fill_color
        self.opacity = opacity



class Line(GenericLine):
    pass



class Path(GenericLine):
    pass



class Rectangle(GenericBox, GenericLine, GenericShape):
    pass



class Polygon(GenericLine, GenericShape):
    pass



class Oval(GenericBox, GenericLine, GenericShape):
    pass



class Arc(GenericBox, GenericLine, GenericShape):
    pass



class Text(GenericBox):
    pass
