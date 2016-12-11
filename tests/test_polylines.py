from unittest import TestCase
from omnicanvas.graphics import Graphic, Polyline
from omnicanvas.exceptions import GeometryError

class PolylineCreationTests(TestCase):

    def test_can_create_polyline(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertIsInstance(polyline, Graphic)
        self.assertEqual(polyline._coordinates, [10, 30, 60, 100, 45, 45, 0, 40])
        self.assertEqual(polyline._line_width, 1)
        self.assertEqual(polyline._line_style, "-")
        self.assertEqual(polyline._line_color, "#000000")
        self.assertEqual(polyline._rotation, (0, 0, 0))
        self.assertEqual(polyline._data, {})


    def test_polygon_repr(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(str(polyline), "<Polyline (4 points)>")
