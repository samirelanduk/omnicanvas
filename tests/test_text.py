from unittest import TestCase
from omnicanvas.graphics import Graphic, Text

class TextCreationTests(TestCase):

    def test_can_create_text(self):
        text = Text(50, 50, "Test")
        self.assertIsInstance(text, Graphic)
        self.assertEqual(text.x, 50)
        self.assertEqual(text.y, 50)
        self.assertEqual(text.line_width, 1)
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



class TextReprTests(TestCase):

    def test_repr_displays_in_full_below_20_chars(self):
        text = Text(50, 50, "01234567890123456789")
        self.assertEqual(str(text), "<Text ('01234567890123456789')>")
        text = Text(50, 50, "012345678901234567890")
        self.assertEqual(str(text), "<Text ('01234567890123456789...')>")
