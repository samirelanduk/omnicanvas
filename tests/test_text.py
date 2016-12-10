from unittest import TestCase
from omnicanvas.graphics import ShapeGraphic, Text

class TextCreationTests(TestCase):

    def test_can_create_text(self):
        text = Text(50, 50, "Test")
        self.assertIsInstance(text, ShapeGraphic)
        self.assertEqual(text._x, 50)
        self.assertEqual(text._y, 50)
        self.assertEqual(text._font_size, 18)
        self.assertEqual(text._horizontal_align, "center")
        self.assertEqual(text._vertical_align, "center")
        self.assertEqual(text._fill_color, "#000000")
        self.assertEqual(text._opacity, 1)
        self.assertEqual(text._line_width, 0)
        self.assertEqual(text._line_style, "-")
        self.assertEqual(text._line_color, "#000000")
        self.assertEqual(text._rotation, (0, 0, 0))
        self.assertEqual(text._data, {})


    def test_text_repr(self):
        text = Text(50, 50, "Test")
        self.assertEqual(str(text), "<Text ('Test')>")


    def test_repr_displays_in_full_below_20_chars(self):
        text = Text(50, 50, "01234567890123456789")
        self.assertEqual(str(text), "<Text ('01234567890123456789')>")
        text = Text(50, 50, "012345678901234567890")
        self.assertEqual(str(text), "<Text ('01234567890123456789...')>")


    def test_text_location_must_be_numeric(self):
        with self.assertRaises(TypeError):
            Text("50", 50, "Test")
        with self.assertRaises(TypeError):
            Text(50, "50", "Test")
        Text(50.5, 50, "Test")
        Text(50, 50.5, "Test")


    def test_can_create_text_with_font_size(self):
        text = Text(50, 50, "Test", font_size=12)
        self.assertEqual(text._font_size, 12)


    def test_font_size_must_be_numeric(self):
        with self.assertRaises(TypeError):
            Text(50, 50, "Test", font_size="12")
        Text(50, 50, "Test", font_size=12.5)


    def test_can_create_text_with_horizontal_align(self):
        text = Text(50, 50, "Test", horizontal_align="left")
        self.assertEqual(text._horizontal_align, "left")


    def test_horizontal_align_must_be_str(self):
        with self.assertRaises(TypeError):
            Text(50, 50, "Test", horizontal_align=None)
        with self.assertRaises(TypeError):
            Text(50, 50, "Test", horizontal_align=23)


    def test_horizontal_align_must_be_valid_text(self):
        with self.assertRaises(ValueError):
            Text(50, 50, "Test", horizontal_align="middle")


    def test_can_create_text_with_vertical_align(self):
        text = Text(50, 50, "Test", vertical_align="top")
        self.assertEqual(text._vertical_align, "top")


    def test_vertical_align_must_be_str(self):
        with self.assertRaises(TypeError):
            Text(50, 50, "Test", vertical_align=None)
        with self.assertRaises(TypeError):
            Text(50, 50, "Test", vertical_align=23)


    def test_vertical_align_must_be_valid_text(self):
        with self.assertRaises(ValueError):
            Text(50, 50, "Test", vertical_align="left")



class TextPropertiesTests(TestCase):

    def test_basic_properties(self):
        text = Text(
         50, 50, "Test", font_size=9,
         vertical_align="top", horizontal_align="left"
        )
        self.assertIs(text.x(), text._x)
        self.assertIs(text.y(), text._y)
        self.assertIs(text.text(), text._text)
        self.assertIs(text.font_size(), text._font_size)
        self.assertIs(text.vertical_align(), text._vertical_align)
        self.assertIs(text.horizontal_align(), text._horizontal_align)


    def test_can_set_location(self):
        text = Text(50, 50, "Test")
        text.x(200)
        self.assertEqual(text.x(), 200)
        text.y(-10)
        self.assertEqual(text.y(), -10)


    def test_set_box_location_must_be_numeric(self):
        text = Text(50, 50, "Test")
        with self.assertRaises(TypeError):
            text.x("10")
        with self.assertRaises(TypeError):
            text.y("20")
        text.x(10.5)
        text.y(10.5)


    def test_can_set_text(self):
        text = Text(50, 50, "Test")
        text.text("NewText")
        self.assertEqual(text.text(), "NewText")


    def test_can_set_font_size(self):
        text = Text(50, 50, "Test", font_size=30)
        text.font_size(40)
        self.assertEqual(text.font_size(), 40)


    def test_set_font_size_must_be_numeric(self):
        text = Text(50, 50, "Test", font_size=30)
        with self.assertRaises(TypeError):
            text.font_size("10")
        text.font_size(10.5)


    def test_can_set_horizontal_align(self):
        text = Text(50, 50, "Test", horizontal_align="left")
        text.horizontal_align("right")
        self.assertEqual(text.horizontal_align(), "right")


    def test_set_horizontal_align_must_be_str(self):
        text = Text(50, 50, "Test", horizontal_align="left")
        with self.assertRaises(TypeError):
            text.horizontal_align(23)


    def test_horizontal_align_must_be_valid_text(self):
        text = Text(50, 50, "Test", horizontal_align="left")
        with self.assertRaises(ValueError):
            text.horizontal_align("middle")


    def test_can_set_vertical_align(self):
        text = Text(50, 50, "Test", vertical_align="top")
        text.vertical_align("bottom")
        self.assertEqual(text.vertical_align(), "bottom")


    def test_set_vertical_align_must_be_str(self):
        text = Text(50, 50, "Test", vertical_align="top")
        with self.assertRaises(TypeError):
            text.vertical_align(23)


    def test_vertical_align_must_be_valid_text(self):
        text = Text(50, 50, "Test", vertical_align="top")
        with self.assertRaises(ValueError):
            text.vertical_align("center")



'''class SvgTests(TestCase):

    def test_can_make_basic_svg(self):
        text = Text(50, 50, "Test")
        self.assertEqual(
         text.to_svg(),
         '<text x="50.0" y="50.0" text-anchor="middle" alignment-baseline="middle"'
         ' style="font-size:18.0;fill:#000000;stroke:#000000;stroke-width:0.0;">Test</text>'
        )


    def test_can_create_text_with_different_horizontal_alignment(self):
        text = Text(50, 50, "Test", horizontal_align="left")
        self.assertEqual(
         text.to_svg(),
         '<text x="50.0" y="50.0" text-anchor="end" alignment-baseline="middle"'
         ' style="font-size:18.0;fill:#000000;stroke:#000000;stroke-width:0.0;">Test</text>'
        )
        text = Text(50, 50, "Test", horizontal_align="right")
        self.assertEqual(
         text.to_svg(),
         '<text x="50.0" y="50.0" text-anchor="start" alignment-baseline="middle"'
         ' style="font-size:18.0;fill:#000000;stroke:#000000;stroke-width:0.0;">Test</text>'
        )


    def test_text_will_check_horizontal_align_value_before_using(self):
        text = Text(50, 50, "Test")
        text.horizontal_align = "start"
        with self.assertRaises(ValueError):
            text.to_svg()


    def test_can_create_text_with_different_vertical_alignment(self):
        text = Text(50, 50, "Test", vertical_align="top")
        self.assertEqual(
         text.to_svg(),
         '<text x="50.0" y="50.0" text-anchor="middle" alignment-baseline="baseline"'
         ' style="font-size:18.0;fill:#000000;stroke:#000000;stroke-width:0.0;">Test</text>'
        )
        text = Text(50, 50, "Test", vertical_align="bottom")
        self.assertEqual(
         text.to_svg(),
         '<text x="50.0" y="50.0" text-anchor="middle" alignment-baseline="hanging"'
         ' style="font-size:18.0;fill:#000000;stroke:#000000;stroke-width:0.0;">Test</text>'
        )


    def test_text_will_check_horizontal_align_value_before_using(self):
        text = Text(50, 50, "Test")
        text.vertical_align = "start"
        with self.assertRaises(ValueError):
            text.to_svg()


    def test_font_size_in_text_svg(self):
        text = Text(50, 50, "Test", font_size=34.4)
        self.assertEqual(
         text.to_svg(),
         '<text x="50.0" y="50.0" text-anchor="middle" alignment-baseline="middle"'
         ' style="font-size:34.4;fill:#000000;stroke:#000000;stroke-width:0.0;">Test</text>'
        )


    def test_can_create_rotated_text_svg(self):
        text = Text(50, 50, "Test", rotation=(200, 200, 45))
        self.assertEqual(
         text.to_svg(),
         '<text x="50.0" y="50.0" text-anchor="middle" alignment-baseline="middle"'
         ' style="font-size:18.0;fill:#000000;stroke:#000000;stroke-width:0.0;"'
         ' transform="rotate(45.0 200.0 200.0)">Test</text>'
        )


    def test_data_in_line_svg(self):
        text = Text(50, 50, "Test", data={"onclick":"func(true);", "a": "b"})
        self.assertIn(
         'onclick="func(true);"',
         text.to_svg()
        )
        self.assertIn(
         'a="b"',
         text.to_svg()
        )'''
