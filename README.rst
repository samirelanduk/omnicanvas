OmniCanvas Documentation
========================

OmniCanvas is a Python canvas which supports basic two-dimensional graphics,
and outputs to various graphics formats - currently just SVG.

Example
-------

  >>> import omnicanvas
  >>> canvas = omnicanvas.Canvas(700, 400)
  >>> canvas.add_rectangle(10, 20, 300, 200, fill_color="#CC0000")
  >>> canvas.graphics[0]
  <Rectangle 300×200 at (10,20)>
  >>> canvas.save("example.svg")

See the the :doc:`examples page <examples>` for more examples, or the full API
for a full listing of features.

Overview
--------

The Canvas
~~~~~~~~~~

The ``Canvas`` class is the first thing you will need to create - it is
the base upon which everything else is created. If you've ever used HTML or GUI
canvases, they work in much the same way.

    >>> import omnicanvas
    >>> canvas = omnicanvas.Canvas(600, 400)
    >>> canvas.width
    600
    >>> canvas.height
    400

Canvases need width and height information, in pixels. You can also specify the
background color:

    >>> canvas = omnicanvas.Canvas(600, 400, background_color="#0000DD")
    >>> canvas.background_color
    '#0000DD'


Graphics
~~~~~~~~

Canvases contain a list of graphics (which all inherit from class
``Graphic``), and it is these objects which make up the image.

Currently, there are four types.

Rectangles
##########

``Rectangle`` objects are... rectangles. Boxes, defined with the
coordinates of their top-left corner, and width and height:

    >>> canvas.add_rectangle(10, 10, 300, 200)
    >>> canvas.graphics[0]
    <Rectangle 300×200 at (10,10)>
    >>> canvas.graphics[0].width
    300

Rectangles inherit from ``ShapeGraphic`` which means they have a fill
color and opacity:

    >>> canvas.add_rectangle(10, 10, 300, 200, fill_color="#3344EE", opacity=0.5)
    >>> canvas.graphics[-1].fill_color
    '#3344EE'
    >>> canvas.graphics[-1].opacity
    0.5

They *also*, like all classes which inherit from class ``Graphic``,
have properties relating to their lines:

    >>> canvas.add_rectangle(10, 10, 300, 200, line_width=2, line_style="--")
    >>> canvas.graphics[-1].line_width
    2
    >>> canvas.graphics[-1].line_style
    '--'
    >>> canvas.graphics[-1].line_color = "#FFFF00"
    >>> canvas.graphics[-1].line_color
    '#FFFF00'

Lines
#####

``Line`` objects are even more straightforward. They are lines defined
by a start coordinate and an end coordinate:

    >>> canvas.add_line(10, 10, 90, 90)
    >>> canvas.x1
    10
    >>> canvas.y1
    10
    >>> canvas.x2
    90
    >>> canvas.y2
    90

Lines inherit directly from ``Graphic`` and have the same properties
relating to line width etc. as above.

Polygons
########

``Polygon`` objects are two-dimensional shapes with an arbitrary number
of points. These are given as a sequence of coordinates:

    >>> canvas.add_polygon(60, 60, 90, 120, 30, 120) # Creates a triangle
    >>> canvas.graphics[-1].coordinates
    [60, 60, 90, 120, 30, 120]
    >>> canvas.graphics[-1].coordinates_to_xy_pairs()
    ((60, 60), (90, 120), (30, 120))

You must supply an even number of points.

Otherwise they behave much like Rectangles - they inherit from
``ShapeGraphic` and :py:class:`.Graphic`` and so have the above
properties relating to fill and border.

Text
####

``Text`` objects are used to hold text. Unlike other Graphics, their
default ``fill_color`` is black, not white, and their default ``line_width`` is
0, not 1.

    >>> canvas.add_text(50, 50, "OmniCanvas is sexy", font_size=32)
    >>> canvas.graphics[-1].text
    'OmniCanvas is sexy'
    >>> canvas.graphics[-1].font_size
    32
    >>> canvas.graphics[-1].fill_color
    '#000000'
    >>> canvas.graphics[-1].line_width
    0

The coordinate given by default will be the centre of the text. This can be
changed by specifying the desired horizontal and vertical alignment:

    >>> canvas.add_text(50, 50, "X", vertical_align="top", horizontal_align="left")


Outputs
~~~~~~~

Once the canvas has been decorated with whatever Graphics you see fit, it can be
saved to file:

    >>> canvas.save("example.svg")

Most browsers will have no trouble displaying SVG files once created.

If you want to get the text of the SVG directly, you can use the ``to_svg()``
method of canvases, which will return this raw text.


Changelog
---------


Release 0.1.0
~~~~~~~~~~~~~

`6 June 2016`

* Canvas with four graphic types:

  * Rectangles
  * Lines
  * Polygons
  * Text

* SVG output
