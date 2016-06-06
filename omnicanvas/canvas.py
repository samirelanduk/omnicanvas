"""This module contains the main Canvas class."""

from .colors import process_color
from . import graphics
from . import svg

class Canvas:
    """A backdrop on which other Graphics objects are painted.

    :param width: The canvas's width in pixels.
    :param height: The canvas's height in pixels.
    :param background_color: The canvas's background colour - the default is\
    white

    .. py:attribute:: width:

        The canvas's width in pixels.

    .. py:attribute:: height:

        The canvas's height in pixels.

    .. py:attribute:: background_color:

        The canvas's background colour.

    .. py:attribute:: graphics:

        A ``list`` of :py:class:`.Graphic` objects on this canvas."""

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

        if background_color is None:
            self.background_color = None
        else:
            self.background_color = process_color(background_color)

        self.graphics = []


    def __repr__(self):
        return "<Canvas %i×%i (%i Graphics)>" % (
         self.width, self.height, len(self.graphics)
        )


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
        :param dict data: Any data to be associated with the Rectangle."""

        self.graphics.append(graphics.Rectangle(*args, **kwargs))


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
        :param dict data: Any data to be associated with the Line."""

        self.graphics.append(graphics.Line(*args, **kwargs))


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
        :param dict data: Any data to be associated with the Polygon."""

        self.graphics.append(graphics.Polygon(*args, **kwargs))


    def add_text(self, *args, **kwargs):
        """Adds a :py:class:`.Text` to the canvas.

        :param x: The x-coordinate of the Text's location.
        :param y: The y-coordinate of the Text's location.
        :param line_width: The width of the Text's outer border.
        :param str line_style: The pattern of the Text's outer border.\
        Acceptable values are ``-`` (default), ``..`` (dotted) or ``--``\
         (dashed).
        :param str line_color: The colour of the Text's outer border.
        :param tuple rotation: Any rotation to be applied, in the format\
        (x of rotation point, y of rotation point, angle).
        :param dict data: Any data to be associated with the Text."""

        self.graphics.append(graphics.Text(*args, **kwargs))


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
