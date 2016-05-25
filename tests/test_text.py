from unittest import TestCase
from omnicanvas.graphics import Graphic, Text

class TextCreationTests(TestCase):

    def test_can_create_text(self):
        text = Text(50, 50, "Test")
        self.assertIsInstance(text, Graphic)
        self.assertEqual(text.x, 50)
        self.assertEqual(text.y, 50)
        self.assertEqual(text.font_size, 18)
        self.assertEqual(text.horizontal_align, "center")
        self.assertEqual(text.vertical_align, "center")
        self.assertEqual(text.line_width, 0)
        self.assertEqual(text.line_style, "-")
        self.assertEqual(text.line_color, "#000000")
        self.assertEqual(str(text), "<Text ('Test')>")


    def test_text_location_must_be_numeric(self):
        with self.assertRaises(TypeError):
            text = Text("50", 50, "Test")
        with self.assertRaises(TypeError):
            text = Text(50, "50", "Test")
        text = Text(50.5, 50, "Test")
        text = Text(50, 50.5, "Test")


    def test_can_create_text_with_font_size(self):
        text = Text(50, 50, "Test", font_size=12)
        self.assertEqual(text.font_size, 12)


    def test_font_size_must_be_numeric(self):
        with self.assertRaises(TypeError):
            text = Text(50, 50, "Test", font_size="12")
        text = Text(50, 50, "Test", font_size=12.5)


    def test_can_create_text_with_horizontal_align(self):
        text = Text(50, 50, "Test", horizontal_align="center")
        self.assertEqual(text.horizontal_align, "center")


    def test_horizontal_align_must_be_str(self):
        with self.assertRaises(TypeError):
            text = Text(50, 50, "Test", horizontal_align=None)
        with self.assertRaises(TypeError):
            text = Text(50, 50, "Test", horizontal_align=23)


    def test_horizontal_align_must_be_valid_text(self):
        with self.assertRaises(ValueError):
            text = Text(50, 50, "Test", horizontal_align="middle")


    def test_can_create_text_with_vertical_align(self):
        text = Text(50, 50, "Test", vertical_align="center")
        self.assertEqual(text.vertical_align, "center")


    def test_vertical_align_must_be_str(self):
        with self.assertRaises(TypeError):
            text = Text(50, 50, "Test", vertical_align=None)
        with self.assertRaises(TypeError):
            text = Text(50, 50, "Test", vertical_align=23)


    def test_vertical_align_must_be_valid_text(self):
        with self.assertRaises(ValueError):
            text = Text(50, 50, "Test", vertical_align="left")



class TextReprTests(TestCase):

    def test_repr_displays_in_full_below_20_chars(self):
        text = Text(50, 50, "01234567890123456789")
        self.assertEqual(str(text), "<Text ('01234567890123456789')>")
        text = Text(50, 50, "012345678901234567890")
        self.assertEqual(str(text), "<Text ('01234567890123456789...')>")



class SvgTests(TestCase):

    def test_can_make_basic_svg(self):
        text = Text(50, 50, "Test")
        self.assertEqual(
         text.to_svg(),
         '<text x="50.0" y="50.0" style="stroke:#000000;stroke-width:0.0;">Test</text>'
        )
