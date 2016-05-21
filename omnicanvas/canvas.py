class Canvas:

    def __init__(self, width, height):
        if not isinstance(width, int):
            raise TypeError("Width must be numeric, not '%s'" % width)
        self.width = width

        if not isinstance(height, int):
            raise TypeError("Height must be numeric, not '%s'" % height)
        self.height = height
        
        self.graphics = []


    def __repr__(self):
        return "<Canvas %i×%i (%i Graphics)>" % (
         self.width, self.height, len(self.graphics)
        )
