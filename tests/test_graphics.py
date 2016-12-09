from unittest import TestCase
from omnicanvas.graphics import Graphic

class GraphicCreationTests(TestCase):

    def test_can_create_graphic(self):
        graphic = Graphic()
        self.assertEqual(graphic._line_width, 1)
        self.assertEqual(graphic._line_style, "-")
        self.assertEqual(graphic._line_color, "#000000")
        self.assertEqual(graphic._rotation, (0, 0, 0))
        self.assertEqual(graphic._data, {})


    def test_can_create_graphic_with_line_width(self):
        graphic = Graphic(line_width=2.4)
        self.assertEqual(graphic._line_width, 2.4)


    def test_line_width_must_be_numeric(self):
        with self.assertRaises(TypeError):
            Graphic(line_width=None)
        with self.assertRaises(TypeError):
            Graphic(line_width="2")
        Graphic(line_width=2.4)
        Graphic(line_width=2)


    def test_can_create_graphic_with_line_style(self):
        graphic = Graphic(line_style="--")
        self.assertEqual(graphic._line_style, "--")


    def test_line_style_must_be_str(self):
        with self.assertRaises(TypeError):
            Graphic(line_style=(1,1))
        with self.assertRaises(TypeError):
            Graphic(line_style=None)


    def test_line_style_must_be_valid(self):
        with self.assertRaises(ValueError):
            Graphic(line_style="")
        with self.assertRaises(ValueError):
            Graphic(line_style="888")


    def test_can_create_graphic_with_line_color(self):
        graphic = Graphic(line_color="#FF0000")
        self.assertEqual(graphic._line_color, "#FF0000")


    def test_graphic_line_will_capitalise_color(self):
        graphic = Graphic(line_color="#ff0000")
        self.assertEqual(graphic._line_color, "#FF0000")


    def test_line_color_must_be_str(self):
        with self.assertRaises(TypeError):
            Graphic(line_color=998877)
        with self.assertRaises(TypeError):
            Graphic(line_color=None)


    def test_line_color_must_be_formatted_correctly(self):
        with self.assertRaises(ValueError):
            Graphic(line_color="FF0000")
        with self.assertRaises(ValueError):
            Graphic(line_color="#FF000")
        with self.assertRaises(ValueError):
            Graphic(line_color="#F00")
        with self.assertRaises(ValueError):
            Graphic(line_color="#FF0G00")


    def test_can_create_graphic_with_rotation(self):
        graphic = Graphic(rotation=(10, 10, 45))
        self.assertEqual(graphic._rotation, (10, 10, 45))


    def test_graphic_rotation_must_be_tuple(self):
        with self.assertRaises(TypeError):
            Graphic(rotation=[10, 10, 45])


    def test_graphic_rotation_must_be_of_length_three(self):
        with self.assertRaises(ValueError):
            Graphic(rotation=(10, 10))
        with self.assertRaises(ValueError):
            Graphic(rotation=(10, 10, 45, 45))


    def test_graphic_rotations_must_be_numeric(self):
        with self.assertRaises(TypeError):
            Graphic(rotation=(10, 10, "10"))
        with self.assertRaises(TypeError):
            Graphic(rotation=(10, "10", 10))
        with self.assertRaises(TypeError):
            Graphic(rotation=("10", 10, 10))
        graphic = Graphic(rotation=(1.5, 1.5, 45.5))


    def test_graphic_rotation_must_be_within_zero_and_360_degrees(self):
        with self.assertRaises(ValueError):
            Graphic(rotation=(10, 10, -1))
        with self.assertRaises(ValueError):
            Graphic(rotation=(10, 10, 400))
        Graphic(rotation=(1.5, 1.5, 0))
        Graphic(rotation=(1.5, 1.5, 360))


    def test_can_create_graphic_with_data(self):
        graphic = Graphic(data={"key": "value"})
        self.assertEqual(graphic._data, {"key": "value"})


    def test_data_must_be_dict(self):
        with self.assertRaises(TypeError):
            Graphic(data=["key", "value"])



class GraphicPropertyTests(TestCase):

    def test_basic_properties(self):
        graphic = Graphic(
         line_width=1, line_style="--", line_color="#FFFFFF",
         rotation=(10, 10, 45), data={"key": "Value"}
        )
        self.assertIs(graphic.line_width(), graphic._line_width)
        self.assertIs(graphic.line_style(), graphic._line_style)
        self.assertIs(graphic.line_color(), graphic._line_color)
        self.assertIs(graphic.rotation(), graphic._rotation)
        self.assertIs(graphic.data(), graphic._data)


    def test_can_set_line_width(self):
        graphic = Graphic(line_width=2.0)
        graphic.line_width(3.5)
        self.assertEqual(graphic.line_width(), 3.5)


    def test_set_line_width_must_be_numeric(self):
        graphic = Graphic(line_width=2.0)
        with self.assertRaises(TypeError):
            graphic.line_width("2")
        graphic.line_width(2.4)
        graphic.line_width(2)


    def test_can_set_line_style(self):
        graphic = Graphic(line_style="--")
        graphic.line_style("-")
        self.assertEqual(graphic.line_style(), "-")


    def test_set_line_style_must_be_str(self):
        graphic = Graphic(line_style="--")
        graphic = Graphic(line_style="--")
        with self.assertRaises(TypeError):
            graphic.line_style((1,1))


    def test_set_line_style_must_be_valid(self):
        graphic = Graphic(line_style="--")
        with self.assertRaises(ValueError):
            graphic.line_style("")
        with self.assertRaises(ValueError):
            graphic.line_style("888")


    def test_can_set_line_color(self):
        graphic = Graphic(line_color="#FF0000")
        graphic.line_color("#00FF00")
        self.assertEqual(graphic.line_color(), "#00FF00")


    def test_set_graphic_line_will_capitalise_color(self):
        graphic = Graphic(line_color="#FF0000")
        graphic.line_color("#ff0000")
        self.assertEqual(graphic._line_color, "#FF0000")


    def test_set_line_color_must_be_str(self):
        graphic = Graphic(line_color="#FF0000")
        with self.assertRaises(TypeError):
            graphic.line_color(998877)


    def test_set_line_color_must_be_formatted_correctly(self):
        graphic = Graphic(line_color="#FF0000")
        with self.assertRaises(ValueError):
            graphic.line_color("FF0000")
        with self.assertRaises(ValueError):
            graphic.line_color("#F0000")
        with self.assertRaises(ValueError):
            graphic.line_color("#F00")
        with self.assertRaises(ValueError):
            graphic.line_color("#FG0000")


    def test_can_rotate_graphic(self):
        graphic = Graphic(rotation=(10, 10, 45))
        graphic.rotate(40, 40, 270)
        self.assertEqual(graphic.rotation(), (40, 40, 270))


    def test_set_graphic_rotations_must_be_numeric(self):
        graphic = Graphic(rotation=(10, 10, 45))
        with self.assertRaises(TypeError):
            graphic.rotate(40, 40, "270")
        with self.assertRaises(TypeError):
            graphic.rotate(40, "40", 270)
        with self.assertRaises(TypeError):
            graphic.rotate("40", 40, 270)
        graphic.rotate(40.5, 40.1, 270.99)


    def test_set_graphic_rotation_must_be_within_zero_and_360_degrees(self):
        graphic = Graphic(rotation=(10, 10, 45))
        with self.assertRaises(ValueError):
            graphic.rotate(40, 40, -1)
        with self.assertRaises(ValueError):
            graphic.rotate(40, 40, 400)
        graphic.rotate(40, 40, 0)
        graphic.rotate(40, 40, 360)



'''class GraphicSvgTests(TestCase):

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


    def test_cannot_produce_rotation_svg_from_invalid_rotation(self):
        graphic = Graphic()
        graphic.rotation = list(graphic.rotation)
        with self.assertRaises(TypeError):
            graphic.rotation_svg()
        graphic.rotation = (1, 1, 1, 1)
        with self.assertRaises(ValueError):
            graphic.rotation_svg()
        graphic.rotation = (1, 1, "1")
        with self.assertRaises(TypeError):
            graphic.rotation_svg()
        graphic.rotation = (1, 1, 400)
        with self.assertRaises(ValueError):
            graphic.rotation_svg()


    def test_data_in_svg(self):
        graphic = Graphic(data={"onclick":"func(true);"})
        self.assertEqual(graphic.data_svg(), ' onclick="func(true);"')
        graphic = Graphic(data={"onclick":"func(true);", "a": "b"})
        self.assertIn(
         'onclick="func(true);"',
         graphic.data_svg()
        )
        self.assertIn(
         'a="b"',
         graphic.data_svg()
        )
        self.assertIn(
         ' ',
         graphic.data_svg()
        )


    def test_data_must_be_dict_for_svg(self):
        graphic = Graphic()
        graphic.data = []
        with self.assertRaises(TypeError):
            graphic.data_svg()'''
