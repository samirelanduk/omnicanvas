from unittest import TestCase
from omnicanvas.graphics import Graphic

class GraphicCreationTests(TestCase):

    def test_can_create_graphic(self):
        graphic = Graphic()
        self.assertEqual(graphic.line_width, 1)
        self.assertEqual(graphic.line_style, "-")


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
