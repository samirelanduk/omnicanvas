"""This module contains various functions usued internally to process colours,
mainly for validation pruposes currently."""

import colorsys

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


def hsl_to_rgb(hue, saturation, lightness):
    """Takes a colour in HSL format and produces an RGB string in the form
    #RRGGBB.

    :param hue: The Hue value (between 0 and 360).
    :param saturation: The Saturation value (between 0 and 100).
    :param lightness: The Lightness value (between 0 and 100).
    :raises ValueError: if any of the three parameters are outside their \
    bounds."""

    if not isinstance(hue, int) and not isinstance(hue, float):
        raise TypeError("hue must be numeric, not '%s'" % hue)
    if not isinstance(saturation, int) and not isinstance(saturation, float):
        raise TypeError("saturation must be numeric, not '%s'" % saturation)
    if not isinstance(lightness, int) and not isinstance(lightness, float):
        raise TypeError("lightness must be numeric, not '%s'" % lightness)
    if not (0 <= hue <= 360):
        raise ValueError("hue must be between 0 and 360, not '%s'" % str(hue))
    if not (0 <= saturation <= 100):
        raise ValueError(
         "saturation must be between 0 and 100, not '%s'" % str(saturation)
        )
    if not (0 <= lightness <= 100):
        raise ValueError(
         "lightness must be between 0 and 100, not '%s'" % str(lightness)
        )

    r, g, b = colorsys.hls_to_rgb(hue / 360, lightness / 100, saturation / 100)
    return ("#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))).upper()
