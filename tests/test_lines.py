from unittest import TestCase
from omnicanvas.graphics import Graphic, Line

class LineCreationTests(TestCase):

    def test_can_create_line(self):
        line = Line(10, 30, 90, 70)
        self.assertIsInstance(line, Graphic)
        self.assertEqual(line._x1, 10)
        self.assertEqual(line._y1, 30)
        self.assertEqual(line._x2, 90)
        self.assertEqual(line._y2, 70)
        self.assertEqual(line._line_width, 1)
        self.assertEqual(line._line_style, "-")
        self.assertEqual(line._line_color, "#000000")
        self.assertEqual(line._rotation, (0, 0, 0))
        self.assertEqual(line._data, {})


    def test_line_repr(self):
        line = Line(10, 30, 90, 70)
        self.assertEqual(str(line), "<Line (10,30) to (90,70)>")


    def test_line_coordinates_must_be_numeric(self):
        with self.assertRaises(TypeError):
            Line("10", 30, 90, 70)
        Line(10.5, 30, 90, 70)
        with self.assertRaises(TypeError):
            Line(10, "30", 90, 70)
        Line(10, 30.5, 90, 70)
        with self.assertRaises(TypeError):
            Line(10, 30, "90", 70)
        Line(10, 30, 90.5, 70)
        with self.assertRaises(TypeError):
            Line(10, 30, 90, "70")
        Line(10, 30, 90, 70.5)



class LinePropertiesTests(TestCase):

    def test_basic_line_properties(self):
        line = Line(10, 30, 90, 70)
        self.assertIs(line.x1(), line._x1)
        self.assertIs(line.y1(), line._y1)
        self.assertIs(line.x2(), line._x2)
        self.assertIs(line.y2(), line._y2)


    def test_can_set_line_coordinates(self):
        line = Line(10, 30, 90, 70)
        line.x1(100)
        self.assertEqual(line.x1(), 100)
        line.y1(100)
        self.assertEqual(line.y1(), 100)
        line.x2(100)
        self.assertEqual(line.x2(), 100)
        line.y2(100)
        self.assertEqual(line.y2(), 100)


    def test_set_line_coordinates_must_be_numeric(self):
        line = Line(10, 30, 90, 70)
        with self.assertRaises(TypeError):
            line.x1("10")
        line.x1(100.5)
        with self.assertRaises(TypeError):
            line.y1("10")
        line.y1(100.5)
        with self.assertRaises(TypeError):
            line.x2("10")
        line.x2(100.5)
        with self.assertRaises(TypeError):
            line.y2("10")
        line.y2(100.5)



'''class LineSvgTests(TestCase):

    def test_can_make_basic_svg(self):
        line = Line(10, 30, 90, 70)
        self.assertEqual(
         line.to_svg(),
         '<line x1="10.0" y1="30.0" x2="90.0" y2="70.0" style="stroke:#000000;" />'
        )


    def test_can_create_rotated_line_svg(self):
        line = Line(10, 30, 90, 70, rotation=(200, 200, 45))
        self.assertEqual(
         line.to_svg(),
         '<line x1="10.0" y1="30.0" x2="90.0" y2="70.0" style="stroke:#000000;"'
         ' transform="rotate(45.0 200.0 200.0)" />'
        )


    def test_data_in_line_svg(self):
        line = Line(10, 30, 90, 70, data={"onclick":"func(true);", "a": "b"})
        self.assertIn(
         'onclick="func(true);"',
         line.to_svg()
        )
        self.assertIn(
         'a="b"',
         line.to_svg()
        )'''
