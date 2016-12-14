"""This module contains the various Graphics objects which can be painted to
the canvas."""

from .colors import process_color
from .exceptions import GeometryError
from . import svg

ALLOWED_LINESTYLES = ("-", "--", "..")

class Graphic:
    """The base class of all Graphics - it would not orindarily need to be
    instantiated at this abstract level.

    Its properties generally relate to lines, as all Graphics have an edge of
    some kind.

    :param str name: An identifable name for the Graphic.
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle), in degrees.
    :param dict data: Any data to be associated with the Graphic."""

    def __init__(self, name=None, line_width=1, line_style="-",
    line_color="#000000", rotation=(0, 0, 0), data=None):
        if not isinstance(name, str) and name is not None:
            raise TypeError("name must be str, not '%s'" % name)
        self._name = name

        if not isinstance(line_width, int) and not isinstance(line_width, float):
            raise TypeError("line_width must be numeric, not '%s'" % line_width)
        self._line_width = line_width

        if not isinstance(line_style, str):
            raise TypeError("Line style must be str, not '%s'" % line_style)
        if line_style not in ALLOWED_LINESTYLES:
            raise ValueError("'%s' is not a valid line style" % line_style)
        self._line_style = line_style

        self._line_color = process_color(line_color)

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
        self._rotation = rotation

        if data is not None and not isinstance(data, dict):
            raise TypeError("Data must be dict, not '%s'" % data)
        self._data = data if data is not None else {}


    def name(self, name=None):
        """An identifable name for the Graphic. Passing a value will update the
        name property.

        :param name: If given, the Graphic's name will be set to this.
        :rtype: ``str``"""
        if name is None:
            return self._name
        else:
            if not isinstance(name, str):
                raise TypeError("name must be str, not '%s'" % name)
            self._name = name


    def line_width(self, line_width=None):
        """The width of the Graphic's edge in pixels. Passing a value will
        update the line_width property.

        :param line_width: If given, the Graphic's line_width will be set to \
        this.
        :rtype: ``int``"""

        if line_width is None:
            return self._line_width
        else:
            if not isinstance(line_width, int) and\
             not isinstance(line_width, float):
                raise TypeError(
                 "line_width must be numeric, not '%s'" % line_width
                )
            self._line_width = line_width


    def line_style(self, line_style=None):
        """The line pattern of the Graphic's edge. Passing a value will update
        the line_style property. Acceptable values are ``-`` (default), ``..`` \
        (dotted) or ``--`` (dashed).

        :param str line_style: If given, the Graphic's line_style will be set to \
        this.
        :rtype: ``str``"""

        if line_style is None:
            return self._line_style
        else:
            if not isinstance(line_style, str):
                raise TypeError("Line style must be str, not '%s'" % line_style)
            if line_style not in ALLOWED_LINESTYLES:
                raise ValueError("'%s' is not a valid line style" % line_style)
            self._line_style = line_style


    def line_color(self, line_color=None):
        """The colur of the Graphic's edge. Passing a value will update
        the line_color property. All colours must be in the form #RRGGBB.

        :param str line_color: If given, the Graphic's line_color will be set to \
        this.
        :rtype: ``str``"""

        if line_color is None:
            return self._line_color
        else:
            self._line_color = process_color(line_color)


    def rotation(self):
        """The rotation applied to the Graphic. It takes the form of a three
        number tuple - ``(pivot_x_coordinate, pivot_y_coordinate, angle)``. The
        angle is in degrees, and works clockwise.

        :rtype: ``tuple``"""

        return self._rotation


    def rotate(self, x_pivot, y_pivot, angle):
        """Rotates the Graphic about a point. The rotation will be clockwise,
        and the angle given must be between 0 and 360.

        Note: rotations do not sum. If you rotate a Graphic once by 30° and then
        again by 100° about the same point, the end result will just be a
        rotation of 100° around that point, *not* 130°. This is because the
        method just sets the Graphic's ``rotation`` property to whatever is
        given.

        :param str x_pivot: The x value of the pivot point.
        :param str y_pivot: The y value of the pivot point.
        :param str angle: The (clockwise) angle of rotation, in degrees.
        :raises ValueError: if the angle is not between 0 and 360."""

        rotation = (x_pivot, y_pivot, angle)
        for value in rotation:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("Rotation values must be numeric, not '%s'" % value)
        if not 0 <= rotation[2] <= 360:
            raise ValueError(
             "Rotation must be between 0 and 360, not %s" % str(rotation[2])
            )
        self._rotation = rotation


    def data(self):
        """Returns any data associated with the Graphic as a ``dict``. This
        ``dict`` is modifiable.

        When rendered as SVG, the data will be turned into ``attribute="value"``
        pairs in the SVG element, and is useful in, among other things,
        assigning JavaScript events to individual elements.

        :rtype: ``dict``"""

        return self._data


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
    :param str name: An identifable name for the Graphic.
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle), in degrees.
    :param dict data: Any data to be associated with the Graphic."""

    def __init__(self, *args, fill_color="#FFFFFF", opacity=1, **kwargs):
        Graphic.__init__(self, *args, **kwargs)

        self._fill_color = process_color(fill_color)

        if not isinstance(opacity, int) and not isinstance(opacity, float):
            raise TypeError("opacity must be numeric, not '%s'" % opacity)
        if not 0 <= opacity <= 1:
            raise ValueError(
             "opacity must be between 0 and 1, not %s" % (str(opacity))
            )
        self._opacity = opacity


    def fill_color(self, fill_color=None):
        """The colour of the shape's interior space. Passing a value will update
        the fill_color property. All colours must be in the form #RRGGBB.

        :param str fill_color: If given, the Shape's fill_color will be set to \
        this.
        :rtype: ``str``"""

        if fill_color is None:
            return self._fill_color
        else:
            self._fill_color = process_color(fill_color)


    def opacity(self, opacity=None):
        """The degree of transparency of the interior space, from 0 to 1 (0
        being invisible). Passing a value will update the opacity property.

        :param floar opacity: If given, the Shape's opacity will be set to \
        this.
        :rtype: ``float``"""

        if opacity is None:
            return self._opacity
        else:
            if not isinstance(opacity, int) and not isinstance(opacity, float):
                raise TypeError("opacity must be numeric, not '%s'" % opacity)
            if not 0 <= opacity <= 1:
                raise ValueError(
                 "opacity must be between 0 and 1, not %s" % (str(opacity))
                )
            self._opacity = opacity


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
    :param str name: An identifable name for the Graphic.
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle), in degrees.
    :param dict data: Any data to be associated with the Box."""

    def __init__(self, x, y, width, height, *args, **kwargs):
        ShapeGraphic.__init__(self, *args, **kwargs)

        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be numeric, not '%s'" % x)
        self._x = x

        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("y must be numeric, not '%s'" % y)
        self._y = y

        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError("width must be numeric, not '%s'" % width)
        self._width = width

        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError("height must be numeric, not '%s'" % height)
        self._height = height


    def x(self, x=None):
        """The x value of the Box's upper-left corner coordinate. Passing a
        value will update the x property.

        :param x: If given, the Box's x value will be set to this.
        :rtype: ``float`` or ``int``"""

        if x is None:
            return self._x
        else:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError("x must be numeric, not '%s'" % x)
            self._x = x


    def y(self, y=None):
        """The y value of the Box's upper-left corner coordinate. Passing a
        value will update the y property.

        :param y: If given, the Box's y value will be set to this.
        :rtype: ``float`` or ``int``"""

        if y is None:
            return self._y
        else:
            if not isinstance(y, int) and not isinstance(y, float):
                raise TypeError("y must be numeric, not '%s'" % y)
            self._y = y


    def width(self, width=None):
        """The width of the Box. Passing a value will update the width.

        :param width: If given, the Box's width will be set to this.
        :rtype: ``float`` or ``int``"""

        if width is None:
            return self._width
        else:
            if not isinstance(width, int) and not isinstance(width, float):
                raise TypeError("width must be numeric, not '%s'" % width)
            self._width = width


    def height(self, height=None):
        """The height of the Box. Passing a value will update the height.

        :param height: If given, the Box's height will be set to this.
        :rtype: ``float`` or ``int``"""

        if height is None:
            return self._height
        else:
            if not isinstance(height, int) and not isinstance(height, float):
                raise TypeError("height must be numeric, not '%s'" % height)
            self._height = height



class Rectangle(BoxGraphic):
    """Base class: :py:class:`BoxGraphic`

    A rectangular graphic, represented as a Rectangle on screen.

    :param x: The x-value of the top-left corner.
    :param y: The y-value of the top-left corner.
    :param width: The Rectangle's width in pixels.
    :param height: The Rectangle's height in pixels.
    :param str fill_color: Defaults to '#FFFFFF'.
    :param opacity: The degree of transparency, from 0 to 1 (0 being\
    invisible).
    :param str name: An identifable name for the Graphic.
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle).
    :param dict data: Any data to be associated with the Shape."""

    def __init__(self, *args, **kwargs):
        BoxGraphic.__init__(self, *args, **kwargs)


    def __repr__(self):
        return "<Rectangle %i×%i at (%i,%i)>" % (
         self.width(), self.height(), self.x(), self.y()
        )


    to_svg = svg.generate_rectangle_svg



class Line(Graphic):
    """Base class: :py:class:`Graphic`

    A straight line between two points.

    :param x1: The x-value of the start point.
    :param y1: The y-value of the start point.
    :param x2: The x-value of the end point.
    :param y2: The y-value of the end point.
    :param str name: An identifable name for the Graphic.
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle), in degrees.
    :param dict data: Any data to be associated with the Graphic."""

    def __init__(self, x1, y1, x2, y2, *args, **kwargs):
        Graphic.__init__(self, *args, **kwargs)
        if not isinstance(x1, int) and not isinstance(x1, float):
            raise TypeError("x1 must be numeric, not '%s'" % x1)
        self._x1 = x1
        if not isinstance(y1, int) and not isinstance(y1, float):
            raise TypeError("y1 must be numeric, not '%s'" % y1)
        self._y1 = y1
        if not isinstance(x2, int) and not isinstance(x2, float):
            raise TypeError("x2 must be numeric, not '%s'" % x2)
        self._x2 = x2
        if not isinstance(y2, int) and not isinstance(y2, float):
            raise TypeError("y2 must be numeric, not '%s'" % y2)
        self._y2 = y2


    def __repr__(self):
        return "<Line (%i,%i) to (%i,%i)>" % (
         self._x1, self._y1, self._x2, self._y2
        )


    def x1(self, x1=None):
        """The x value of the Line's start point coordinate. Passing a
        value will update the x1 property.

        :param x1: If given, the Line's x1 value will be set to this.
        :rtype: ``float`` or ``int``"""

        if x1 is None:
            return self._x1
        else:
            if not isinstance(x1, int) and not isinstance(x1, float):
                raise TypeError("x1 must be numeric, not '%s'" % x1)
            self._x1 = x1


    def y1(self, y1=None):
        """The y value of the Line's start point coordinate. Passing a
        value will update the y1 property.

        :param y1: If given, the Line's y1 value will be set to this.
        :rtype: ``float`` or ``int``"""

        if y1 is None:
            return self._y1
        else:
            if not isinstance(y1, int) and not isinstance(y1, float):
                raise TypeError("y1 must be numeric, not '%s'" % y1)
            self._y1 = y1


    def x2(self, x2=None):
        """The x value of the Line's end point coordinate. Passing a
        value will update the x2 property.

        :param x2: If given, the Line's x2 value will be set to this.
        :rtype: ``float`` or ``int``"""

        if x2 is None:
            return self._x2
        else:
            if not isinstance(x2, int) and not isinstance(x2, float):
                raise TypeError("x2 must be numeric, not '%s'" % x2)
            self._x2 = x2


    def y2(self, y2=None):
        """The y value of the Line's end point coordinate. Passing a
        value will update the y2 property.

        :param y2: If given, the Line's y2 value will be set to this.
        :rtype: ``float`` or ``int``"""

        if y2 is None:
            return self._y2
        else:
            if not isinstance(y2, int) and not isinstance(y2, float):
                raise TypeError("y2 must be numeric, not '%s'" % y2)
            self._y2 = y2


    to_svg = svg.generate_line_svg



class Polygon(ShapeGraphic):
    """Base class: :py:class:`ShapeGraphic`

    Polygons are shapes with an arbitrary number of vertices.

    :param \*coordinates: The coordinates as a sequence of alternating x and y \
    values.
    :param str fill_color: Defaults to '#FFFFFF'.
    :param opacity: The degree of transparency, from 0 to 1 (0 being\
    invisible).
    :param str name: An identifable name for the Graphic.
    :param line_width: Defaults to 1.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle), in degrees.
    :param dict data: Any data to be associated with the Polygon.
    :raises ValueError: if an odd number of coordinate values are given.
    :raises GeometryError: if there are fewer than three vertices."""

    def __init__(self, *coordinates, **kwargs):
        ShapeGraphic.__init__(self, **kwargs)

        for value in coordinates:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("'%s' is an invalid coordinate" % value)
        if len(coordinates) % 2 != 0:
            raise ValueError("There must be an even number of coordinates")
        if len(coordinates) < 6:
            raise GeometryError("There must be at least three vertices")
        self._coordinates = list(coordinates)


    def __repr__(self):
        return("<Polygon (%i points)>" % (len(self._coordinates) / 2))


    def coordinates(self, xy_pairs=False):
        """Returns the coordinates of the Polygon. By default they will be
        returned as a single ``tuple`` of alternating x and y values.

        ``(x1, y1, x2, y2, x3, y3...)``

        However, you can optionally have it return them as a tuple of xy
        two-tuple pairs with the ``xy_pairs`` argument.

        ``((x1, y1), (x2, y2), (x3, y3)...)``

        :param bool xy_pairs: if True, the coordinates will be returned as xy\
        pairs (see above).
        :rtype: ``tuple``"""

        if xy_pairs:
            return tuple(zip(self._coordinates[:-1:2], self._coordinates[1::2]))
        else:
            return tuple(self._coordinates)


    def add_vertex(self, x, y):
        """Adds a vertex to the Polygon. The vertex will be added at the end of
        the list of vertices.

        :param x: The x-value of the new vertex's coordinate.
        :param y: The y-value of the new vertex's coordinate."""

        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be numeric, not '%s'" % x)
        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("y must be numeric, not '%s'" % y)
        self._coordinates.append(x)
        self._coordinates.append(y)


    def remove_vertex(self, index):
        """Removes a the vertex at the specified index from the Polygon.

        :param int index: The index of the vertex to be removed.
        :raises GeometryError: if removing a vertex would leave the Polygon\
        with fewer than three vertices."""

        if len(self._coordinates) <= 6:
            raise GeometryError("There must be at least three vertices")
        if not isinstance(index, int):
            raise TypeError("Vertex index must be int")
        self._coordinates.pop(index * 2)
        self._coordinates.pop(index * 2)


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
    values are ``top``, ``middle`` (default) and ``bottom``.
    :param str fill_color: Defaults to '#FFFFFF'.
    :param opacity: The degree of transparency, from 0 to 1 (0 being\
    invisible).
    :param str name: An identifable name for the Graphic.
    :param line_width: Defaults to 0.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle), in degrees.
    :param dict data: Any data to be associated with the Text."""

    def __init__(self, x, y, text, *args, font_size=18, fill_color="#000000",
     line_width=0, horizontal_align="center", vertical_align="center", **kwargs):
        ShapeGraphic.__init__(self, *args, fill_color=fill_color, line_width=line_width, **kwargs)

        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be numeric, not '%s'" % x)
        self._x = x

        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("y must be numeric, not '%s'" % y)
        self._y = y

        self._text = text

        if not isinstance(font_size, int) and not isinstance(font_size, float):
            raise TypeError("Font size must be numeric, not '%s'" % font_size)
        self._font_size = font_size

        if not isinstance(horizontal_align, str):
            raise TypeError(
             "horizontal align must be str, not '%s'" % horizontal_align
            )
        if horizontal_align not in ("left", "center", "right"):
            raise ValueError(
             "'%s' is not a valid horizontal alignment" % horizontal_align
            )
        self._horizontal_align = horizontal_align

        if not isinstance(vertical_align, str):
            raise TypeError(
             "vertical align must be str, not '%s'" % vertical_align
            )
        if vertical_align not in ("top", "center", "bottom"):
            raise ValueError(
             "'%s' is not a valid vertical alignment" % vertical_align
            )
        self._vertical_align = vertical_align


    def __repr__(self):
        text = str(self._text)
        return "<Text ('%s')>" % (
         text if len(text) < 21 else text[:20] + "..."
        )


    def x(self, x=None):
        """The x-value of the Text's location. How this point relates to the
        Text's location is determined by ``horizontal_align`` and
        ``vertical_align``. Passing a value will update the x property.

        :param x: If given, the Text's x value will be set to this.
        :rtype: ``float`` or ``int``"""

        if x is None:
            return self._x
        else:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError("x must be numeric, not '%s'" % x)
            self._x = x


    def y(self, y=None):
        """The y-value of the Text's location. How this point relates to the
        Text's location is determined by ``horizontal_align`` and
        ``vertical_align``. Passing a value will update the y property.

        :param y: If given, the Text's y value will be set to this.
        :rtype: ``float`` or ``int``"""

        if y is None:
            return self._y
        else:
            if not isinstance(y, int) and not isinstance(y, float):
                raise TypeError("y must be numeric, not '%s'" % y)
            self._y = y


    def text(self, text=None):
        """The text that the the Graphic displays. If something other than a
        string is passed, the ``__str__`` representation of that object will
        be used. Passing a value will update the text property.

        :param text: If given, the Text's text value will be set to this.
        :rtype: ``str``"""
        if text is None:
            return self._text
        else:
            self._text = text


    def font_size(self, font_size=None):
        """The text's font size, in pt. Passing a value will update the
        font_size.

        :param font_size: If given, the font_size value will be set to this.
        :rtype: ``int`` or ``float``"""

        if font_size is None:
            return self._font_size
        else:
            if not isinstance(font_size, int) and not isinstance(font_size, float):
                raise TypeError("font_size must be numeric, not '%s'" % font_size)
            self._font_size = font_size


    def horizontal_align(self, horizontal_align=None):
        """The horizontal alignment of the text. If ``center`` the coordinate
        will represent the middle of the Text. If ``left`` the Text will be to
        the left of the coordinate and if ``right`` the Text will be to the
        right. Passing a value will update the horizontal_align.

        :param str horizontal_align: If given, the horizontal_align value will \
        be set to this.
        :raises ValueError: if you try to set horizontal_align to something \
        other than the three allowed values.
        :rtype: str"""

        if horizontal_align is None:
            return self._horizontal_align
        else:
            if not isinstance(horizontal_align, str):
                raise TypeError(
                 "horizontal align must be str, not '%s'" % horizontal_align
                )
            if horizontal_align not in ("left", "center", "right"):
                raise ValueError(
                 "'%s' is not a valid horizontal alignment" % horizontal_align
                )
            self._horizontal_align = horizontal_align


    def vertical_align(self, vertical_align=None):
        """The vertical alignment of the text. If ``middle`` the coordinate
        will represent the middle of the Text. If ``top`` the Text will be to
        the abovef the coordinate and if ``bottom`` the Text will be below.
        Passing a value will update the vertical_align.

        :param str vertical_align: If given, the vertical_align value will be \
        set to this.
        :raises ValueError: if you try to set vertical_align to something other\
        than the three allowed values.
        :rtype: str"""
        if vertical_align is None:
            return self._vertical_align
        else:
            if not isinstance(vertical_align, str):
                raise TypeError(
                 "vertical align must be str, not '%s'" % vertical_align
                )
            if vertical_align not in ("top", "middle", "bottom"):
                raise ValueError(
                 "'%s' is not a valid vertical alignment" % vertical_align
                )
            self._vertical_align = vertical_align


    to_svg = svg.generate_text_svg



class Polyline(Graphic):
    """Base class: :py:class:`Graphic`

    Polylines are lines with an arbitrary number of vertices. Unlike Polygons,
    the last vertex is not joined to the first one, and so they have no
    interior space.

    :param \*coordinates: The coordinates as a sequence of alternating x and y \
    values.
    :param line_width: Defaults to 1.
    :param str name: An identifable name for the Graphic.
    :param str line_style: The line pattern. Acceptable values are\
    ``-`` (default), ``..`` (dotted) or ``--`` (dashed).
    :param str line_color: Defaults to '#000000'.
    :param tuple rotation: Any rotation to be applied, in the format\
    (x of rotation point, y of rotation point, angle), in degrees.
    :param dict data: Any data to be associated with the Polygon.
    :raises ValueError: if an odd number of coordinate values are given.
    :raises GeometryError: if there are fewer than two vertices."""

    def __init__(self, *coordinates, **kwargs):
        Graphic.__init__(self, **kwargs)

        for value in coordinates:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("'%s' is an invalid coordinate" % value)
        if len(coordinates) % 2 != 0:
            raise ValueError("There must be an even number of coordinates")
        if len(coordinates) < 4:
            raise GeometryError("There must be at least two vertices")
        self._coordinates = list(coordinates)


    def __repr__(self):
        return("<Polyline (%i points)>" % (len(self._coordinates) / 2))


    def coordinates(self, xy_pairs=False):
        """Returns the coordinates of the Polyline. By default they will be
        returned as a single ``tuple`` of alternating x and y values.

        ``(x1, y1, x2, y2, x3, y3...)``

        However, you can optionally have it return them as a tuple of xy
        two-tuple pairs with the ``xy_pairs`` argument.

        ``((x1, y1), (x2, y2), (x3, y3)...)``

        :param bool xy_pairs: if True, the coordinates will be returned as xy\
        pairs (see above).
        :rtype: ``tuple``"""

        if xy_pairs:
            return tuple(zip(self._coordinates[:-1:2], self._coordinates[1::2]))
        else:
            return tuple(self._coordinates)


    def add_vertex(self, x, y):
        """Adds a vertex to the Polyline. The vertex will be added at the end of
        the list of vertices.

        :param x: The x-value of the new vertex's coordinate.
        :param y: The y-value of the new vertex's coordinate."""

        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be numeric, not '%s'" % x)
        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("y must be numeric, not '%s'" % y)
        self._coordinates.append(x)
        self._coordinates.append(y)


    def remove_vertex(self, index):
        """Removes a the vertex at the specified index from the Polyline.

        :param int index: The index of the vertex to be removed.
        :raises GeometryError: if removing a vertex would leave the Polyline\
        with fewer than two vertices."""

        if len(self._coordinates) <= 4:
            raise GeometryError("There must be at least two vertices")
        if not isinstance(index, int):
            raise TypeError("Vertex index must be int")
        self._coordinates.pop(index * 2)
        self._coordinates.pop(index * 2)


    to_svg = svg.generate_polyline_svg
