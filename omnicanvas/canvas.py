class Canvas:

    def __init__(self, width, height):
        self.graphics = []
        self.width = width
        self.height = height


    def __repr__(self):
        return "<Canvas %i×%i (%i Graphics)>" % (
         self.width, self.height, len(self.graphics)
        )
