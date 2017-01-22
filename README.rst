OmniCanvas Documentation
========================

OmniCanvas is a Python canvas which supports basic two-dimensional graphics,
and outputs to various graphics formats - currently just SVG.

Example
-------

  >>> import omnicanvas
  >>> canvas = omnicanvas.Canvas(700, 400)
  >>> canvas.add_rectangle(10, 20, 300, 200, fill_color="#CC0000")
  >>> canvas.graphics()[0]
  <Rectangle 300×200 at (10,20)>
  >>> canvas.save("example.svg")

See the the examples for more examples, or the full API
for a full listing of features.

Installing
----------

pip
~~~

OmniCanvas can be installed using pip:

``$ pip3 install omnicanvas``

OmniCanvas is written for Python 3, and does not support Python 2.

If you get permission errors, try using ``sudo``:

``$ sudo pip3 install omnicanvas``


Development
~~~~~~~~~~~

The repository for OmniCanvas, containing the most recent iteration, can be
found `here <http://github.com/samirelanduk/omnicanvas/>`_. To clone the
OmniCanvas repository directly from there, use:

``git clone git://github.com/samirelanduk/omnicanvas.git``


Requirements
~~~~~~~~~~~~

OmniCanvas currently has no external dependencies, and is pure Python.


Overview
--------

The Canvas
~~~~~~~~~~

The ``Canvas`` class is the first thing you will need to create - it is
the base upon which everything else is created. If you've ever used HTML or GUI
canvases, they work in much the same way.

    >>> import omnicanvas
    >>> canvas = omnicanvas.Canvas(600, 400)
    >>> canvas.width()
    600
    >>> canvas.height()
    400

Canvases need width and height information, in pixels. You can also specify the
background color:

    >>> canvas = omnicanvas.Canvas(600, 400, background_color="#0000DD")
    >>> canvas.background_color()
    '#0000DD'


Graphics
~~~~~~~~

Canvases contain a list of graphics (which all inherit from class
``Graphic``), and it is these objects which make up the image.

Currently, there are the following types.

Rectangles
##########

``Rectangle`` objects are... rectangles. Boxes, defined with the
coordinates of their top-left corner, and width and height:

    >>> canvas.add_rectangle(10, 10, 300, 200)
    >>> canvas.graphics()[0]
    <Rectangle 300×200 at (10,10)>
    >>> canvas.graphics()[0].width()
    300

Rectangles inherit from ``ShapeGraphic`` which means they have a fill
color and opacity:

    >>> canvas.add_rectangle(10, 10, 300, 200, fill_color="#3344EE", opacity=0.5)
    >>> canvas.graphics()[-1].fill_color()
    '#3344EE'
    >>> canvas.graphics()[-1].opacity()
    0.5

They *also*, like all classes which inherit from class ``Graphic``,
have properties relating to their lines:

    >>> canvas.add_rectangle(10, 10, 300, 200, line_width=2, line_style="--")
    >>> canvas.graphics()[-1].line_width()
    2
    >>> canvas.graphics()[-1].line_style()
    '--'
    >>> canvas.graphics()[-1].line_color("#FFFF00")
    >>> canvas.graphics()[-1].line_color()
    '#FFFF00'

Ovals
#####

:py:class:`.Oval` objects represent circles and ovals generally. They are
defined by the bounding rectangle around them.

>>> canvas.add_oval(10, 10, 300, 200)
>>> canvas.graphics()[0]
<Oval 300×200 at (10,10)>
>>> canvas.graphics()[0].width()
300

Like Rectangles they also have properties relating to their interior space and
their edges.

Lines
#####

``Line`` objects are even more straightforward. They are lines defined
by a start coordinate and an end coordinate:

    >>> canvas.add_line(10, 10, 90, 90)
    >>> canvas.x1()
    10
    >>> canvas.y1()
    10
    >>> canvas.x2()
    90
    >>> canvas.y2()
    90

Lines inherit directly from ``Graphic`` and have the same properties
relating to line width etc. as above.

Polygons
########

``Polygon`` objects are two-dimensional shapes with an arbitrary number
of points. These are given as a sequence of coordinates:

    >>> canvas.add_polygon(60, 60, 90, 120, 30, 120) # Creates a triangle
    >>> canvas.graphics()[-1].coordinates()
    (60, 60, 90, 120, 30, 120)
    >>> canvas.graphics()[-1].coordinates(xy_pairs=True)
    ((60, 60), (90, 120), (30, 120))

You must supply an even number of points, and there must be at least three
vertices.

Otherwise they behave much like Rectangles - they inherit from
``Graphic`` and so have the above
properties relating to fill and border.

Text
####

``Text`` objects are used to hold text. Unlike other Graphics, their
default ``fill_color`` is black, not white, and their default ``line_width`` is
0, not 1.

    >>> canvas.add_text(50, 50, "OmniCanvas is sexy", font_size=32)
    >>> canvas.graphics()[-1].text()
    'OmniCanvas is sexy'
    >>> canvas.graphics()[-1].font_size()
    32
    >>> canvas.graphics()[-1].fill_color()
    '#000000'
    >>> canvas.graphics()[-1].line_width()
    0

The coordinate given by default will be the centre of the text. This can be
changed by specifying the desired horizontal and vertical alignment:

    >>> canvas.add_text(50, 50, "X", vertical_align="top", horizontal_align="left")


Polylines
#########

These are very similar to ``Polygon``, except the last vertex is not
joined to the first one, and so they have no interior space. They are just lines
with an arbitrary number of vertices.

They behave very similarly to Polygons:

    >>> canvas.add_polyline(60, 60, 90, 120, 30, 120)
    >>> canvas.graphics()[-1].coordinates()
    (60, 60, 90, 120, 30, 120)
    >>> canvas.graphics()[-1].coordinates(xy_pairs=True)
    ((60, 60), (90, 120), (30, 120))


Graphic Retrieval
~~~~~~~~~~~~~~~~~

All of the above graphic adding methods will return the graphic they have just
added, if you need a reference to it later.

>>> rectangle = canvas.add_rectangle(10, 10, 300, 200)
>>> rectangle
<Rectangle 300×200 at (10,10)>

Additionally, all graphics can be given names, which can then be used to
retrieve them from the Canvas using two methods -
``~.canvas.Canvas.get_graphic_by_name`` and
``~.canvas.Canvas.get_graphics_by_name``:

>>> canvas.add_line(10, 10, 90, 90, name="Line 1")
>>> canvas.add_line(20, 10, 90, 90, name="Line 2")
>>> canvas.add_line(10, 20, 90, 90, name="A Line")
>>> canvas.add_line(20, 20, 90, 90, name="A Line")
>>> canvas.get_graphic_by_name("Line 1")
<Line (10,10) to (90,70)>
>>> canvas.get_graphic_by_name("Line 2")
<Line (20,10) to (90,70)>
>>> canvas.get_graphic_by_name("A Line")
<Line (10,20) to (90,70)>
>>> canvas.get_graphics_by_name("A Line")
[<Line (10,20) to (90,70)>, <Line (20,20) to (90,70)>]



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

Release 0.3.0
~~~~~~~~~~~~~

`22 January 2017`

* Added Oval Graphic.
* Graphic objects can now be reordered by the Canvas.
* There are now pleasant colour constants.

Release 0.2.2
~~~~~~~~~~~~~

`15 December 2016`

* Fixed inconsistency in whether the central vertical alignment is 'middle' or 'center'


Release 0.2.1
~~~~~~~~~~~~~

`14 December 2016`

* Graphics adding methods now return a reference to the graphic just added.
* Added names to graphics, and methods for retrieving them from the canvas by name.


Release 0.2.0
~~~~~~~~~~~~~

`12 December 2016`

* All attributes are now method properties.
* Added function for converting HSL colours to RGB strings.
* Added Polyline Graphic.


Release 0.1.0
~~~~~~~~~~~~~

`6 June 2016`

* Canvas with four graphic types:

  * Rectangles
  * Lines
  * Polygons
  * Text

* SVG output
