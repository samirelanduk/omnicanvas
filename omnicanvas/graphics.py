from .colors import _process_color

class Graphic:

    def __init__(self, line_width=1):
        if not isinstance(line_width, int) and not isinstance(line_width, float):
            raise TypeError("line_width must be numeric, not '%s'" % line_width)
        self.line_width = line_width



class ShapeGraphic(Graphic):

    def __init__(self, fill_color="#FFFFFF", opacity=1):
        self.fill_color = _process_color(fill_color)

        if not isinstance(opacity, int) and not isinstance(opacity, float):
            raise TypeError("opacity must be numeric, not '%s'" % opacity)
        if not 0 <= opacity <= 1:
            raise ValueError(
             "opacity must be between 0 and 1, not %s" % (str(opacity))
            )
        self.opacity=opacity



class BoxGraphic(ShapeGraphic):

    def __init__(self, x, y, width, height):
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
    pass
