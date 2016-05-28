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

Table of Contents
-----------------

.. toctree ::

    installing
    overview
    examples
    api
    changelog
