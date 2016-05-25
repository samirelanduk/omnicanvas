from unittest import TestCase
from omnicanvas.graphics import Graphic, Line

class LineCreationTests(TestCase):

    def test_can_create_line(self):
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


    def test_line_coordinates_must_be_numeric(self):
        with self.assertRaises(TypeError):
            line = Line("10", 30, 90, 70)
        line = Line(10.5, 30, 90, 70)
        with self.assertRaises(TypeError):
            line = Line(10, "30", 90, 70)
        line = Line(10, 30.5, 90, 70)
        with self.assertRaises(TypeError):
            line = Line(10, 30, "90", 70)
        line = Line(10, 30, 90.5, 70)
        with self.assertRaises(TypeError):
            line = Line(10, 30, 90, "70")
        line = Line(10, 30, 90, 70.5)



class LineSvgTests(TestCase):

    def test_can_make_basic_svg(self):
        line = Line(10, 30, 90, 70)
        self.assertEqual(
         line.to_svg(),
         '<line x1="10.0" y1="30.0" x2="90.0" y2="70.0" style="stroke:#000000;" />'
        )
