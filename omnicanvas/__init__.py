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
        return _width


    def height(self):
        return _height
