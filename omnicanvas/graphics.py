"""This module contains the various Graphics objects which can be painted to
the canvas."""

from .colors import process_color
from . import svg

class Graphic:
    """The base class of all Graphics - it would not generally need to be
    instantiated at this abstract level.

    Its properties generally relate to lines, as all Graphics have an edge of
    some kind.

    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle).
    :param dict data: Any data to be associated with the Graphic.

    .. py:attribute:: line_width:

        The width of the Graphic's line in pixels.

    .. py:attribute:: line_style:

        The line pattern. Acceptable values are ``-`` (default), ``..`` \
        (dotted) or ``--`` (dashed).

    .. py:attribute:: line_color:

        The colour of the Graphic's line.

    .. py:attribute:: rotation:

        Any rotation to be applied, in the format (x of rotation point, y of\
        rotation point, angle). For example, to rotate the Graphic 45 degrees
        anti-clockwise about the point (100, 200) you would supply
        ``(100, 200, 315)``.

    .. py:attribute:: data:

        Any data to be associated with the Graphic, as a ``dict``."""

    def __init__(self, line_width=1, line_style="-", line_color="#000000",
     rotation=(0, 0, 0), data=None):
        if not isinstance(line_width, int) and not isinstance(line_width, float):
            raise TypeError("line_width must be numeric, not '%s'" % line_width)
        self.line_width = line_width

        if not isinstance(line_style, str):
            raise TypeError("Line style must be str, not '%s'" % line_style)
        if line_style not in ("-", "--", ".."):
            raise ValueError("'%s' is not a valid line style" % line_style)
        self.line_style = line_style

        self.line_color = process_color(line_color)

        if not isinstance(rotation, tuple):
            raise TypeError("Rotations must be tuples, not '%s'" % str(rotation))
        if len(rotation) != 3:
            raise ValueError(
             "Rotations must be tuples of length 3, not %i" % len(rotation)
            )
        for value in rotation:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("Rotation values must be numeric, not '%s'" % value)
        if not 0 <= rotation[2] <= 360:
            raise ValueError(
             "Rotation must be between 0 and 360, not %s" % str(rotation[2])
            )
        self.rotation = rotation

        if data is not None and not isinstance(data, dict):
            raise TypeError("Data must be dict, not '%s'" % data)
        self.data = data if data is not None else {}


    graphic_svg = svg.generate_graphic_svg
    rotation_svg = svg.generate_rotation_svg
    data_svg = svg.generate_data_svg



class ShapeGraphic(Graphic):
    """Base class: :py:class:`Graphic`

    Shapes are Graphics which have an interior space of some kind, which in
    practice is most Graphics which aren't just lines.

    Its properties relate to the appearence of this interior space. It would not
    generally be instantiated directly.

    :param str fill_color: Defaults to '#FFFFFF'.
    :param opacity: The degree of transparency, from 0 to 1 (0 being\
    invisible).
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle).
    :param dict data: Any data to be associated with the Shape.

    .. py:attribute:: fill_color:

        The colour of the Shape's interior, as a hex string.

    .. py:attribute:: opacity:

        The degree of transparency of the Shape's interior, from 1.0 (fully\
        visible) to 0.0 (completely invisible).

    .. py:attribute:: line_width:

        The width of the Shape's border in pixels.

    .. py:attribute:: line_style:

        The border line pattern. Acceptable values are ``-`` (default), ``..`` \
        (dotted) or ``--`` (dashed).

    .. py:attribute:: line_color:

        The colour of the Shape's border.

    .. py:attribute:: rotation:

        Any rotation to be applied, in the format (x of rotation point, y of\
        rotation point, angle). For example, to rotate the Shape 45 degrees
        anti-clockwise about the point (100, 200) you would supply
        ``(100, 200, 315)``.

    .. py:attribute:: data:

        Any data to be associated with the Shape, as a ``dict``."""

    def __init__(self, *args, fill_color="#FFFFFF", opacity=1, **kwargs):
        Graphic.__init__(self, *args, **kwargs)

        self.fill_color = process_color(fill_color)

        if not isinstance(opacity, int) and not isinstance(opacity, float):
            raise TypeError("opacity must be numeric, not '%s'" % opacity)
        if not 0 <= opacity <= 1:
            raise ValueError(
             "opacity must be between 0 and 1, not %s" % (str(opacity))
            )
        self.opacity=opacity


    shape_svg = svg.generate_shape_svg



class BoxGraphic(ShapeGraphic):
    """Base class: :py:class:`ShapeGraphic`

    BoxGraphics are shapes which are either a box themselves (such as
    :py:class:`.Rectangle`) or are defined by some kind of bounding box. It
    would not generally be instantiated directly.

    :param x: The x-value of the top-left corner.
    :param y: The y-value of the top-left corner.
    :param width: The Box's width in pixels.
    :param height: The Box's height in pixels.
    :param str fill_color: Defaults to '#FFFFFF'.
    :param opacity: The degree of transparency, from 0 to 1 (0 being\
    invisible).
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle).
    :param dict data: Any data to be associated with the Box.

    .. py:attribute:: x:

        The x-value of the top-left corner.

    .. py:attribute:: y:

        The y-value of the top-left corner.

    .. py:attribute:: width:

        The Box's width in pixels.

    .. py:attribute:: height:

        The Box's height in pixels.

    .. py:attribute:: fill_color:

        The colour of the Box's interior, as a hex string.

    .. py:attribute:: opacity:

        The degree of transparency of the Box's interior, from 1.0 (fully\
        visible) to 0.0 (completely invisible).

    .. py:attribute:: line_width:

        The width of the Box's border in pixels.

    .. py:attribute:: line_style:

        The border line pattern. Acceptable values are ``-`` (default), ``..`` \
        (dotted) or ``--`` (dashed).

    .. py:attribute:: line_color:

        The colour of the Box's border.

    .. py:attribute:: rotation:

        Any rotation to be applied, in the format (x of rotation point, y of\
        rotation point, angle). For example, to rotate the Box 45 degrees
        anti-clockwise about the point (100, 200) you would supply
        ``(100, 200, 315)``.

    .. py:attribute:: data:

        Any data to be associated with the Box, as a ``dict``."""

    def __init__(self, x, y, width, height, *args, **kwargs):
        ShapeGraphic.__init__(self, *args, **kwargs)

        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be numeric, not '%s'" % x)
        self.x = x

        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("y must be numeric, not '%s'" % y)
        self.y = y

        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError("width must be numeric, not '%s'" % width)
        self.width = width

        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError("height must be numeric, not '%s'" % height)
        self.height = height



class Rectangle(BoxGraphic):
    """Base class: :py:class:`BoxGraphic`

    A rectangular graphic. Not sure what else to say about this to be honest.

    :param x: The x-value of the top-left corner.
    :param y: The y-value of the top-left corner.
    :param width: The Rectangle's width in pixels.
    :param height: The Rectangle's height in pixels.
    :param str fill_color: Defaults to '#FFFFFF'.
    :param opacity: The degree of transparency, from 0 to 1 (0 being\
    invisible).
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle).
    :param dict data: Any data to be associated with the Shape.

    .. py:attribute:: x:

        The x-value of the top-left corner.

    .. py:attribute:: y:

        The y-value of the top-left corner.

    .. py:attribute:: width:

        The Rectangle's width in pixels.

    .. py:attribute:: height:

        The Rectangle's height in pixels.

    .. py:attribute:: fill_color:

        The colour of the Rectangle's interior, as a hex string.

    .. py:attribute:: opacity:

        The degree of transparency of the Rectangle's interior, from 1.0 (fully\
        visible) to 0.0 (completely invisible).

    .. py:attribute:: line_width:

        The width of the Rectangle's border in pixels.

    .. py:attribute:: line_style:

        The border line pattern. Acceptable values are ``-`` (default), ``..`` \
        (dotted) or ``--`` (dashed).

    .. py:attribute:: line_color:

        The colour of the Rectangle's border.

    .. py:attribute:: rotation:

        Any rotation to be applied, in the format (x of rotation point, y of\
        rotation point, angle). For example, to rotate the Rectangle 45 degrees
        anti-clockwise about the point (100, 200) you would supply
        ``(100, 200, 315)``.

    .. py:attribute:: data:

        Any data to be associated with the Rectangle, as a ``dict``."""

    def __init__(self, *args, **kwargs):
        BoxGraphic.__init__(self, *args, **kwargs)


    def __repr__(self):
        return "<Rectangle %i×%i at (%i,%i)>" % (
         self.width, self.height, self.x, self.y
        )


    to_svg = svg.generate_rectangle_svg



class Line(Graphic):
    """Base class: :py:class:`Graphic`

    A straight line between two points.

    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle).
    :param dict data: Any data to be associated with the Graphic.

    .. py:attribute:: x1:

        The x-value of the start point.

    .. py:attribute:: y1:

        The y-value of the start point.

    .. py:attribute:: x2:

        The x-value of the end point.

    .. py:attribute:: y2:

        The y-value of the end point.

    .. py:attribute:: line_width:

        The width of the Line in pixels.

    .. py:attribute:: line_style:

        The Line pattern. Acceptable values are ``-`` (default), ``..`` \
        (dotted) or ``--`` (dashed).

    .. py:attribute:: line_color:

        The colour of the Line.

    .. py:attribute:: rotation:

        Any rotation to be applied, in the format (x of rotation point, y of\
        rotation point, angle). For example, to rotate the Line 45 degrees
        anti-clockwise about the point (100, 200) you would supply
        ``(100, 200, 315)``.

    .. py:attribute:: data:

        Any data to be associated with the Line, as a ``dict``."""

    def __init__(self, x1, y1, x2, y2, *args, **kwargs):
        Graphic.__init__(self, *args, **kwargs)
        if not isinstance(x1, int) and not isinstance(x1, float):
            raise TypeError("x1 must be numeric, not '%s'" % x1)
        self.x1 = x1
        if not isinstance(y1, int) and not isinstance(y1, float):
            raise TypeError("y1 must be numeric, not '%s'" % y1)
        self.y1 = y1
        if not isinstance(x2, int) and not isinstance(x2, float):
            raise TypeError("x2 must be numeric, not '%s'" % x2)
        self.x2 = x2
        if not isinstance(y2, int) and not isinstance(y2, float):
            raise TypeError("y2 must be numeric, not '%s'" % y2)
        self.y2 = y2


    def __repr__(self):
        return "<Line (%i,%i) to (%i,%i)>" % (
         self.x1, self.y1, self.x2, self.y2
        )


    to_svg = svg.generate_line_svg



class Polygon(ShapeGraphic):
    """Base class: :py:class:`ShapeGraphic`

    Polygons are shapes with an arbitrary number of vertices.

    :param \*coordinates: The coordinates as a sequence of alternating x and y \
    values.
    :param str fill_color: Defaults to '#FFFFFF'.
    :param opacity: The degree of transparency, from 0 to 1 (0 being\
    invisible).
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle).
    :param dict data: Any data to be associated with the Polygon.

    .. py:attribute:: coordinates:

        A sequence of values representing the coordinates of the Polygon's \
        vertices, as alternating x and y values. For example, \
        ``(50, 50, 70, 100, 30, 70)`` would be the coordinates of a small\
        triangle.

    .. py:attribute:: fill_color:

        The colour of the Polygon's interior, as a hex string.

    .. py:attribute:: opacity:

        The degree of transparency of the Polygon's interior, from 1.0 (fully\
        visible) to 0.0 (completely invisible).

    .. py:attribute:: line_width:

        The width of the Polygon's border in pixels.

    .. py:attribute:: line_style:

        The border line pattern. Acceptable values are ``-`` (default), ``..`` \
        (dotted) or ``--`` (dashed).

    .. py:attribute:: line_color:

        The colour of the Polygon's border.

    .. py:attribute:: rotation:

        Any rotation to be applied, in the format (x of rotation point, y of\
        rotation point, angle). For example, to rotate the Polygon 45 degrees\
        anti-clockwise about the point (100, 200) you would supply
        ``(100, 200, 315)``.

    .. py:attribute:: data:

        Any data to be associated with the Polygon, as a ``dict``."""

    def __init__(self, *coordinates, **kwargs):
        ShapeGraphic.__init__(self, **kwargs)

        for value in coordinates:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("'%s' is an invalid coordinate" % value)
        if len(coordinates) % 2 != 0:
            raise ValueError("There must be an even number of coordinates")
        self.coordinates = list(coordinates)


    def __repr__(self):
        return("<Polygon (%i points)>" % (len(self.coordinates) / 2))


    def coordinates_to_xy_pairs(self):
        """Returns the polygon's coordinates as a sequence of tuples, where
        each tuple is in the form (x value, y value)."""

        if len(self.coordinates) % 2 != 0:
            raise ValueError(
             "Cannot process polygon coordiantes with odd number of values"
            )
        return tuple(zip(self.coordinates[:-1:2], self.coordinates[1::2]))


    to_svg = svg.generate_polygon_svg



class Text(ShapeGraphic):
    """Base class: :py:class:`ShapeGraphic`

    Graphics of textual information.

    :param x: The Text's x location.
    :param y: The Text's y location.
    :param str text: The text to display.
    :param font_size: The font size of the Text when displayed.
    :param horizontal_align: The horizontal alignment of the Text. Acceptable\
    values are ``left``, ``center`` (default) and ``right``.
    :param vertical_align: The vertical alignment of the Text. Acceptable\
    values are ``top``, ``center`` (default) and ``bottom``.
    :param str fill_color: Defaults to '#FFFFFF'.
    :param opacity: The degree of transparency, from 0 to 1 (0 being\
    invisible).
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle).
    :param dict data: Any data to be associated with the Text.

    .. py:attribute:: x:

        The x-value of the Text.

    .. py:attribute:: y:

        The y-value of the Text.

    .. py:attribute:: font_size:

        The font size of the Text.

    .. py:attribute:: horizontal_align:

        Determines what the coordinate of the Text represents. If ``center``
        the coordinate will represent the middle of the Text. If ``left`` the
        Text will be to the left of the coordinate and if ``right`` the Text
        will be to the right.

    .. py:attribute:: vertical_align:

        Determines what the coordinate of the Text represents. If ``center``
        the coordinate will represent the middle of the Text. If ``top`` the
        Text will be above the coordinate and if ``bottom`` the Text
        will be below it.

    .. py:attribute:: fill_color:

        The colour of the Text as a hex string.

    .. py:attribute:: opacity:

        The degree of transparency of the Text, from 1.0 (fully\
        visible) to 0.0 (completely invisible).

    .. py:attribute:: line_width:

        The width of the Text's border in pixels.

    .. py:attribute:: line_style:

        The Text border line pattern. Acceptable values are ``-`` (default), \
        ``..`` (dotted) or ``--`` (dashed).

    .. py:attribute:: line_color:

        The colour of the Text's border.

    .. py:attribute:: rotation:

        Any rotation to be applied, in the format (x of rotation point, y of\
        rotation point, angle). For example, to rotate the Text 45 degrees
        anti-clockwise about the point (100, 200) you would supply
        ``(100, 200, 315)``.

    .. py:attribute:: data:

        Any data to be associated with the Text, as a ``dict``."""

    def __init__(self, x, y, text, *args, font_size=18, fill_color="#000000",
     line_width=0, horizontal_align="center", vertical_align="center", **kwargs):
        ShapeGraphic.__init__(self, *args, fill_color=fill_color, line_width=line_width, **kwargs)

        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be numeric, not '%s'" % x)
        self.x = x

        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("y must be numeric, not '%s'" % y)
        self.y = y

        self.text = text

        if not isinstance(font_size, int) and not isinstance(font_size, float):
            raise TypeError("Font size must be numeric, not '%s'" % font_size)
        self.font_size = font_size

        if not isinstance(horizontal_align, str):
            raise TypeError(
             "horizontal align must be str, not '%s'" % horizontal_align
            )
        if horizontal_align not in ("left", "center", "right"):
            raise ValueError(
             "'%s' is not a valid horizontal alignment" % horizontal_align
            )
        self.horizontal_align = horizontal_align

        if not isinstance(vertical_align, str):
            raise TypeError(
             "vertical align must be str, not '%s'" % vertical_align
            )
        if vertical_align not in ("top", "center", "bottom"):
            raise ValueError(
             "'%s' is not a valid vertical alignment" % vertical_align
            )
        self.vertical_align = vertical_align


    def __repr__(self):
        return "<Text ('%s')>" % (
         str(self.text) if len(str(self.text)) < 21 else str(self.text)[:20] + "..."
        )


    to_svg = svg.generate_text_svg
