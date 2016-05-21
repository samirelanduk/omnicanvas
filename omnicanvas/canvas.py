class Canvas:

    def __init__(self, width, height, background_color=None):
        if isinstance(width, float):
            width = round(width)
        if not isinstance(width, int):
            raise TypeError("Width must be numeric, not '%s'" % width)
        self.width = width

        if isinstance(height, float):
            height = round(height)
        if not isinstance(height, int):
            raise TypeError("Height must be numeric, not '%s'" % height)
        self.height = height

        self.background_color = _process_color(background_color)
        self.graphics = []


    def __repr__(self):
        return "<Canvas %i×%i (%i Graphics)>" % (
         self.width, self.height, len(self.graphics)
        )



def _process_color(color):
    if color is None:
        return None
    elif not isinstance(color, str):
        raise TypeError("Color must be str, not '%s'" % color)
    elif not _is_valid_color(color):
        raise ValueError("'%s' is not a valid color" % color)
    else:
        return color.upper()


def _is_valid_color(color):
    if not color:
        return False
    if color[0] != "#":
        return False
    if len(color) != 7:
        return False
    for char in color[1:]:
        if char.upper() not in "0123456789ABCDEF":
            return False
    return True
