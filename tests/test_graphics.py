from unittest import TestCase
from omnicanvas.graphics import Graphic

class GraphicCreationTests(TestCase):

    def test_can_create_graphic(self):
        graphic = Graphic()
        self.assertEqual(graphic.line_width, 1)


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
