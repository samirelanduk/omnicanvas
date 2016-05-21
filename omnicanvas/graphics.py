class Graphic:
    pass



class ShapeGraphic(Graphic):
    pass



class BoxGraphic(ShapeGraphic):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height



class Rectangle(BoxGraphic):
    pass
