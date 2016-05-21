def _process_color(color):
    if not isinstance(color, str):
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
