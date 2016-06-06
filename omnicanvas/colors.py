"""This module contains various functions usued internally to process colours,
mainly for validation pruposes currently."""

def process_color(color):
    """Raises exceptions if a colour does not meet requirements.

    :param str color: The colour to check.
    :raises TypeError: if the colour is not a string.
    :raises ValueError: if the colour is not valid."""

    if not isinstance(color, str):
        raise TypeError("Color must be str, not '%s'" % color)
    elif not is_valid_color(color):
        raise ValueError("'%s' is not a valid color" % color)
    else:
        return color.upper()


def is_valid_color(color):
    """Checks that a given string represents a valid hex colour.

    :param str color: The color to check.
    :rtype: ``bool``"""

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
