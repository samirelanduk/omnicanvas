Overview
--------

The Canvas
~~~~~~~~~~

The :py:class:`.Canvas` class is the first thing you will need to create - it is
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
