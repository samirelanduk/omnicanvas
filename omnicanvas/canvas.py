"""This module contains the main Canvas class."""

from .colors import process_color
from . import graphics
from . import svg

class Canvas:
    """A backdrop on which other :py:class:`.Graphic` objects are painted.

    :param width: The canvas's width in pixels.
    :param height: The canvas's height in pixels.
    :param background_color: The canvas's background colour - the default is\
    white"""

    def __init__(self, width, height, background_color=None):
        if isinstance(width, float):
            width = round(width)
        if not isinstance(width, int):
            raise TypeError("Width must be numeric, not '%s'" % width)
        self._width = width

        if isinstance(height, float):
            height = round(height)
        if not isinstance(height, int):
            raise TypeError("Height must be numeric, not '%s'" % height)
        self._height = height

        if background_color is None:
            self._background_color = None
        else:
            self._background_color = process_color(background_color)

        self._graphics = []


    def __repr__(self):
        return "<Canvas %i×%i (%i Graphics)>" % (
         self._width, self._height, len(self._graphics)
        )


    def width(self, width=None):
        """The canvas's width in pixels. Passing a value will update the width
        property.

        :param width: If given, the canvas's width will be set to this.
        :rtype: ``int``"""

        if width is None:
            return self._width
        else:
            if isinstance(width, float):
                width = round(width)
            if not isinstance(width, int):
                raise TypeError("Width must be numeric, not '%s'" % width)
            self._width = width


    def height(self, height=None):
        """The canvas's height in pixels. Passing a value will update the height
        property.

        :param height: If given, the canvas's height will be set to this.
        :rtype: ``int``"""

        if height is None:
            return self._height
        else:
            if isinstance(height, float):
                height = round(height)
            if not isinstance(height, int):
                raise TypeError("Height must be numeric, not '%s'" % height)
            self._height = height


    def background_color(self, background_color=None):
        """The canvas's background colour, as a hex string. Passing a value will
        update the background_color property (as a hex string).

        :param str background_color: If given, the canvas's background_color \
        will be set to this.
        :rtype: ``str``"""

        if background_color is None:
            return self._background_color
        else:
            self._background_color = process_color(background_color)


    def graphics(self):
        """A list of all the :py:class:`.Graphic` objects on this canvas.

        :rtype: ``list``"""

        return list(self._graphics)


    def get_graphic_by_name(self, name):
        """Searches the canvas's :py:class:`.Graphic` objects and returns the
        first one with a matching name. Returns ``None`` if there are no
        matches.

        :param str name: The name to search by.
        :rtype: str"""

        if not isinstance(name, str):
            raise TypeError(
             "Can only search for str name, not '%s'" % str(name)
            )
        for graphic in self.graphics():
            if graphic.name() == name:
                return graphic


    def get_graphics_by_name(self, name):
        """Searches the canvas's :py:class:`.Graphic` objects and returns all
        the ones with a matching name. Returns an empty list if there are no
        matches.

        :param str name: The name to search by.
        :returns: ``list`` of :py:class:`.Graphic`"""

        if not isinstance(name, str):
            raise TypeError(
             "Can only search for str name, not '%s'" % str(name)
            )
        return [g for g in self.graphics() if g.name() == name]


    def add_rectangle(self, *args, **kwargs):
        """Adds a :py:class:`.Rectangle` to the canvas.

        :param x: The x-coordinate of the Rectangle's upper left corner.
        :param y: The y-coordinate of the Rectangle's upper left corner.
        :param width: The Rectangle's width.
        :param height: The Rectangle's height.
        :param str fill_color: The Rectangle's interior colour.
        :param opacity: The degree of transparency, from 0 to 1 (0 being\
        invisible).
        :param line_width: The width of the edge of the Rectangle in pixels.
        :param str line_style: The pattern of the edges. Acceptable values are\
        ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
        :param str line_color: The colour of the edge.
        :param tuple rotation: Any rotation to be applied, in the format\
        (x of rotation point, y of rotation point, angle).
        :param dict data: Any data to be associated with the Rectangle.
        :rtype: :py:class:`.Rectangle`"""

        self._graphics.append(graphics.Rectangle(*args, **kwargs))
        return self._graphics[-1]


    def add_line(self, *args, **kwargs):
        """Adds a :py:class:`.Line` to the canvas.

        :param x1: The x-coordinate of the Line's start point.
        :param y1: The y-coordinate of the Line's start point.
        :param x2: The x-coordinate of the Line's end point.
        :param y2: The y-coordinate of the Line's end point.
        :param line_width: The width of the Line in pixels.
        :param str line_style: The pattern of the Line. Acceptable values are\
        ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
        :param str line_color: The colour of the Line.
        :param tuple rotation: Any rotation to be applied, in the format\
        (x of rotation point, y of rotation point, angle).
        :param dict data: Any data to be associated with the Line.
        :rtype: :py:class:`.Line`"""

        self._graphics.append(graphics.Line(*args, **kwargs))
        return self._graphics[-1]


    def add_polygon(self, *args, **kwargs):
        """Adds a :py:class:`.Polygon` to the canvas.

        :param \*points: The alternating x and y values of the Polygon's\
        corners.
        :param str fill_color: The Polygon's interior colour.
        :param opacity: The degree of transparency, from 0 to 1 (0 being\
        invisible).
        :param line_width: The width of the edge of the Polygon in pixels.
        :param str line_style: The pattern of the edges. Acceptable values are\
        ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
        :param str line_color: The colour of the edge.
        :param tuple rotation: Any rotation to be applied, in the format\
        (x of rotation point, y of rotation point, angle).
        :param dict data: Any data to be associated with the Polygon.
        :rtype: :py:class:`.Polygon`"""

        self._graphics.append(graphics.Polygon(*args, **kwargs))
        return self._graphics[-1]


    def add_text(self, *args, **kwargs):
        """Adds a :py:class:`.Text` to the canvas.

        :param x: The Text's x location.
        :param y: The Text's y location.
        :param str text: The text to display.
        :param font_size: The font size of the Text when displayed.
        :param horizontal_align: The horizontal alignment of the Text. Acceptable\
        values are ``left``, ``center`` (default) and ``right``.
        :param vertical_align: The vertical alignment of the Text. Acceptable\
        values are ``top``, ``middle`` (default) and ``bottom``.
        :param str fill_color: Defaults to '#FFFFFF'.
        :param opacity: The degree of transparency, from 0 to 1 (0 being\
        invisible).
        :param line_width: Defaults to 0.
        :param str line_style: The line pattern. Acceptable values are\
        ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
        :param str line_color: Defaults to '#000000'.
        :param tuple rotation: Any rotation to be applied, in the format\
        (x of rotation point, y of rotation point, angle), in degrees.
        :param dict data: Any data to be associated with the Text.
        :rtype: :py:class:`.Text`"""

        self._graphics.append(graphics.Text(*args, **kwargs))
        return self._graphics[-1]


    def add_polyline(self, *args, **kwargs):
        """Adds a :py:class:`.Polyline` to the canvas.

        :param \*points: The alternating x and y values of the Polyline's\
        corners.
        :param line_width: The width of the edge of the Polyline in pixels.
        :param str line_style: The pattern of the edges. Acceptable values are\
        ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
        :param str line_color: The colour of the edge.
        :param tuple rotation: Any rotation to be applied, in the format\
        (x of rotation point, y of rotation point, angle).
        :param dict data: Any data to be associated with the Polyline.
        :rtype: :py:class:`.Polyline`"""

        self._graphics.append(graphics.Polyline(*args, **kwargs))
        return self._graphics[-1]


    def save(self, path):
        """Saves the canvas to file as an SVG file.

        :param str path: The location and filename to save to."""

        with open(path, "w") as f:
            f.write(self.to_svg())


    to_svg = svg.generate_canvas_svg
    """Returns the SVG text of the canvas.

    Any ``data`` attributes of the Graphics contained will be rendered as SVG
    attributes.

    :rtype: ``str``"""
