Examples
--------

The UK Union Flag
~~~~~~~~~~~~~~~~~

The following code will produce an SVG file of the British flag:

.. code-block:: python

    import math
    import omnicanvas

    def create_union_flag(height):
        # The union flag is twice as wide as it is high
        canvas = omnicanvas.Canvas(height * 2, height, background_color="#000066")

        #This is the length of the diagonal of the flag, with Pythagoras
        diagonal_length = math.sqrt((height ** 2) + ((height * 2) ** 2))

        # This is the angle of the diagonal strips from the horizontal
        # tan(θ) = opposite / adjacent, so θ = atan(opposite / adjacent)
        diagonal_angle = math.degrees(math.atan((height / 2) / height))

        # Add The diagonal white strips
        canvas.add_rectangle(
         height - (height * 0.1),
         (height / 2) - (diagonal_length / 2),
         height * 0.2,
         diagonal_length,
         line_width=0,
         rotation=(
          height, height / 2, 270 + diagonal_angle
         )
        )
        canvas.add_rectangle(
         height - (height * 0.1),
         (height / 2) - (diagonal_length / 2),
         height * 0.2,
         diagonal_length,
         line_width=0,
         rotation=(
          height, height / 2, 90 - diagonal_angle
         )
        )

        # Add diagonal red strips - these'll be partly covered by the white cross
        canvas.add_rectangle(
         height - (height / 15),
         (height / 2) - (diagonal_length / 2),
         height / 15,
         diagonal_length / 2,
         line_width=0,
         fill_color="#CC0000",
         rotation=(
          height, height / 2, 90 - diagonal_angle
         )
        )
        canvas.add_rectangle(
         height - (height / 15),
         (height / 2) - (diagonal_length / 2),
         height / 15,
         diagonal_length / 2,
         line_width=0,
         fill_color="#CC0000",
         rotation=(
          height, height / 2, 270 - diagonal_angle
         )
        )
        canvas.add_rectangle(
         height - (height / 15),
         (height / 2) - (diagonal_length / 2),
         height / 15,
         diagonal_length / 2,
         line_width=0,
         fill_color="#CC0000",
         rotation=(
          height, height / 2, 270 + diagonal_angle
         )
        )
        canvas.add_rectangle(
         height - (height / 15),
         (height / 2) - (diagonal_length / 2),
         height / 15,
         diagonal_length / 2,
         line_width=0,
         fill_color="#CC0000",
         rotation=(
          height, height / 2, 90 + diagonal_angle
         )
        )

        # Add the white cross
        canvas.add_rectangle(
         height - (height / 6),
         0,
         height / 3,
         height,
         line_width=0
        )
        canvas.add_rectangle(
         0,
         (height / 2) - (height / 6),
         height * 2,
         height / 3,
         line_width=0
        )

        # Add the red cross
        canvas.add_rectangle(
         height - (height / 10),
         0,
         height / 5,
         height,
         line_width=0,
         fill_color="#CC0000",
        )
        canvas.add_rectangle(
         0,
         (height / 2) - (height / 10),
         height * 2,
         height / 5,
         line_width=0,
         fill_color="#CC0000",
        )

        return canvas

    # Create a flag of height 360px (and so width 720px)
    create_union_flag(360).save("ukflag.svg")
