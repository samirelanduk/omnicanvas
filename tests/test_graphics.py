from unittest import TestCase
from omnicanvas.graphics import Graphic

class GraphicCreationTests(TestCase):

    def test_can_create_graphic(self):
        graphic = Graphic()
        self.assertEqual(graphic.line_width, 1)
        self.assertEqual(graphic.line_style, "-")
        self.assertEqual(graphic.line_color, "#000000")
        self.assertEqual(graphic.rotation, (0, 0, 0))


    def test_can_create_graphic_with_line_width(self):
        graphic = Graphic(line_width=2.4)
        self.assertEqual(graphic.line_width, 2.4)


    def test_line_width_must_be_numeric(self):
        with self.assertRaises(TypeError):
            graphic = Graphic(line_width=None)
        with self.assertRaises(TypeError):
            graphic = Graphic(line_width="2")
        graphic = Graphic(line_width=2.4)
        graphic = Graphic(line_width=2)


    def test_can_create_graphic_with_line_style(self):
        graphic = Graphic(line_style="--")
        self.assertEqual(graphic.line_style, "--")


    def test_line_style_must_be_str(self):
        with self.assertRaises(TypeError):
            graphic = Graphic(line_style=(1,1))
        with self.assertRaises(TypeError):
            graphic = Graphic(line_style=None)


    def test_line_style_must_be_valid(self):
        with self.assertRaises(ValueError):
            graphic = Graphic(line_style="")
        with self.assertRaises(ValueError):
            graphic = Graphic(line_style="888")


    def test_can_create_graphic_with_line_color(self):
        graphic = Graphic(line_color="#FF0000")
        self.assertEqual(graphic.line_color, "#FF0000")


    def test_graphic_line_will_capitalise_color(self):
        graphic = Graphic(line_color="#ff0000")
        self.assertEqual(graphic.line_color, "#FF0000")


    def test_line_color_must_be_str(self):
        with self.assertRaises(TypeError):
            graphic = Graphic(line_color=998877)
        with self.assertRaises(TypeError):
            graphic = Graphic(line_color=None)


    def test_line_color_must_be_formatted_correctly(self):
        with self.assertRaises(ValueError):
            graphic = Graphic(line_color="FF0000")
        with self.assertRaises(ValueError):
            graphic = Graphic(line_color="#FF000")
        with self.assertRaises(ValueError):
            graphic = Graphic(line_color="#F00")
        with self.assertRaises(ValueError):
            graphic = Graphic(line_color="#FF0G00")


    def test_can_create_graphic_with_rotation(self):
        graphic = Graphic(rotation=(10, 10, 45))
        self.assertEqual(graphic.rotation, (10, 10, 45))


    def test_graphic_rotation_must_be_tuple(self):
        with self.assertRaises(TypeError):
            graphic = Graphic(rotation=[10, 10, 45])


    def test_graphic_rotation_must_be_of_length_three(self):
        with self.assertRaises(ValueError):
            graphic = Graphic(rotation=(10, 10))
        with self.assertRaises(ValueError):
            graphic = Graphic(rotation=(10, 10, 45, 45))


    def test_graphic_rotations_are_numeric(self):
        with self.assertRaises(TypeError):
            graphic = Graphic(rotation=(10, 10, "10"))
        with self.assertRaises(TypeError):
            graphic = Graphic(rotation=(10, "10", 10))
        with self.assertRaises(TypeError):
            graphic = Graphic(rotation=("10", 10, 10))
        graphic = Graphic(rotation=(1.5, 1.5, 45.5))


    def test_graphic_rotation_must_be_within_zero_and_360_degrees(self):
        with self.assertRaises(ValueError):
            graphic = Graphic(rotation=(10, 10, -1))
        with self.assertRaises(ValueError):
            graphic = Graphic(rotation=(10, 10, 400))
        graphic = Graphic(rotation=(1.5, 1.5, 0))
        graphic = Graphic(rotation=(1.5, 1.5, 360))


class GraphicSvgTests(TestCase):

    def test_graphic_can_produce_stroke_svg(self):
        graphic = Graphic()
        self.assertEqual(graphic.graphic_svg(), "stroke:#000000;")
        graphic = Graphic(line_color="#ABCDEF")
        self.assertEqual(graphic.graphic_svg(), "stroke:#ABCDEF;")


    def test_graphic_can_produce_line_width_svg(self):
        graphic = Graphic(line_width=2.4)
        self.assertEqual(
         graphic.graphic_svg(),
         "stroke:#000000;stroke-width:2.4;"
        )


    def test_graphic_can_produce_line_pattern_svg(self):
        graphic = Graphic(line_style="--")
        self.assertEqual(
         graphic.graphic_svg(),
         "stroke:#000000;stroke-dasharray:10.0,5.0;"
        )
        graphic = Graphic(line_style="..")
        self.assertEqual(
         graphic.graphic_svg(),
         "stroke:#000000;stroke-dasharray:1.0,2.0;"
        )


    def test_line_pattern_changes_with_line_width(self):
        graphic = Graphic(line_style="--", line_width=2.5)
        self.assertEqual(
         graphic.graphic_svg(),
         "stroke:#000000;stroke-width:2.5;stroke-dasharray:25.0,12.5;"
        )
        graphic = Graphic(line_style="..", line_width=2.5)
        self.assertEqual(
         graphic.graphic_svg(),
         "stroke:#000000;stroke-width:2.5;stroke-dasharray:2.5,5.0;"
        )
        graphic = Graphic(line_style="--", line_width=10)
        self.assertEqual(
         graphic.graphic_svg(),
         "stroke:#000000;stroke-width:10.0;stroke-dasharray:100.0,50.0;"
        )
        graphic = Graphic(line_style="..", line_width=10)
        self.assertEqual(
         graphic.graphic_svg(),
         "stroke:#000000;stroke-width:10.0;stroke-dasharray:10.0,20.0;"
        )


    def test_cannot_use_invalid_line_style(self):
        graphic = Graphic(line_style="--")
        graphic.line_style = "8--8"
        with self.assertRaises(ValueError):
            graphic.graphic_svg()


    def test_can_produce_rotation(self):
        graphic = Graphic()
        self.assertEqual(graphic.rotation_svg(), "")
        graphic = Graphic(rotation=(10, 10, 90))
        self.assertEqual(
         graphic.rotation_svg(),
         ' transform="rotate(90.0 10.0 10.0)"'
        )
