from unittest import TestCase
from omnicanvas.graphics import Graphic, Line

class LineCreationTests(TestCase):

    def test_can_create_rectangle(self):
        line = Line(10, 30, 90, 70)
        self.assertIsInstance(line, Graphic)
        self.assertEqual(line.x1, 10)
        self.assertEqual(line.y1, 30)
        self.assertEqual(line.x2, 90)
        self.assertEqual(line.y2, 70)
        self.assertEqual(line.line_width, 1)
        self.assertEqual(line.line_style, "-")
        self.assertEqual(line.line_color, "#000000")
        self.assertEqual(str(line), "<Line (10,30) to (90,70)>")
