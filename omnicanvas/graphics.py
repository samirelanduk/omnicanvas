class Graphic:
    pass



class ShapeGraphic(Graphic):
    pass



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
