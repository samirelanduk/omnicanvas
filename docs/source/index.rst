omnicanvas Documentation
========================

omnicanvas is a Python package for easily drawing to canvas based displays. It
currently supports drawing to SVG, and future versions will add support for
HTML canvas, Tkinter canvas, and a variety of image formats.

Example Code
------------

  >>> import omnicanvas
  >>> canvas = omnicanvas.Canvas(500, 300, background_color="#A8CCF0")
  >>> canvas.draw_rectangle(10, 10, 200, 200, fill_color="#D92626", line_width=0)
  >>> canvas.draw_rectangle(290, 90, 200, 200, fill_color="#144BB8", line_width=0)
  >>> canvas.draw_oval(150, 50, 200, 200, fill_color="#00FF00", opacity=0.4)
  >>> canvas.save("svg", "example.svg")

This would produce:

.. figure:: example.svg
    :align: center



omnicanvas also supports text, lines, arcs, and more. For more details see the
:doc:`overview` or the :doc:`full API docs<api>`.


Table of Contents
-----------------

.. toctree::
    installing
    overview
    api
    changelog
