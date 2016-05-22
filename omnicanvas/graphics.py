from .colors import _process_color

class Graphic:

    def __init__(self, line_width=1, line_style="-", line_color="#000000"):
        if not isinstance(line_width, int) and not isinstance(line_width, float):
            raise TypeError("line_width must be numeric, not '%s'" % line_width)
        self.line_width = line_width

        if not isinstance(line_style, str):
            raise TypeError("Line style must be str, not '%s'" % line_style)
        if line_style not in ("-", "--", ".."):
            raise ValueError("'%s' is not a valid line style" % line_style)
        self.line_style = line_style

        self.line_color = _process_color(line_color)



class ShapeGraphic(Graphic):

    def __init__(self, *args, fill_color="#FFFFFF", opacity=1, **kwargs):
        Graphic.__init__(self, *args, **kwargs)

        self.fill_color = _process_color(fill_color)

        if not isinstance(opacity, int) and not isinstance(opacity, float):
            raise TypeError("opacity must be numeric, not '%s'" % opacity)
        if not 0 <= opacity <= 1:
            raise ValueError(
             "opacity must be between 0 and 1, not %s" % (str(opacity))
            )
        self.opacity=opacity



class BoxGraphic(ShapeGraphic):

    def __init__(self, x, y, width, height, *args, **kwargs):
        ShapeGraphic.__init__(self, *args, **kwargs)

        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be numeric, not '%s'" % x)
        self.x = x

        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("y must be numeric, not '%s'" % y)
        self.y = y

        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError("width must be numeric, not '%s'" % width)
        self.width = width

        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError("height must be numeric, not '%s'" % height)
        self.height = height



class Rectangle(BoxGraphic):

    def __init__(self, *args, **kwargs):
        BoxGraphic.__init__(self, *args, **kwargs)


    def __repr__(self):
        return "<Rectangle %i×%i at (%i,%i)>" % (
         self.width, self.height, self.x, self.y
        )



class Line(Graphic):

    def __init__(self, x1, y1, x2, y2, *args, **kwargs):
        Graphic.__init__(self, *args, **kwargs)
        if not isinstance(x1, int) and not isinstance(x1, float):
            raise TypeError("x1 must be numeric, not '%s'" % x1)
        self.x1 = x1
        if not isinstance(y1, int) and not isinstance(y1, float):
            raise TypeError("y1 must be numeric, not '%s'" % y1)
        self.y1 = y1
        if not isinstance(x2, int) and not isinstance(x2, float):
            raise TypeError("x2 must be numeric, not '%s'" % x2)
        self.x2 = x2
        if not isinstance(y2, int) and not isinstance(y2, float):
            raise TypeError("y2 must be numeric, not '%s'" % y2)
        self.y2 = y2


    def __repr__(self):
        return "<Line (%i,%i) to (%i,%i)>" % (
         self.x1, self.y1, self.x2, self.y2
        )



class Polygon(ShapeGraphic):

    def __init__(self, *coordinates, **kwargs):
        ShapeGraphic.__init__(self, **kwargs)
        self.coordinates = list(coordinates)


    def __repr__(self):
        return("<Polygon (%i points)>" % (len(self.coordinates) / 2))
