from unittest import TestCase
from omnicanvas.graphics import ShapeGraphic, Polygon

class PolygonCreationTests(TestCase):

    def test_can_create_polyon(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertIsInstance(polygon, ShapeGraphic)
        self.assertEqual(polygon.coordinates, [10, 30, 60, 100, 45, 45, 0, 40])
        self.assertEqual(polygon.fill_color, "#FFFFFF")
        self.assertEqual(polygon.opacity, 1)
        self.assertEqual(polygon.line_width, 1)
        self.assertEqual(polygon.line_style, "-")
        self.assertEqual(polygon.line_color, "#000000")
        self.assertEqual(str(polygon), "<Polygon (4 points)>")


    def test_polygon_coordinates_must_be_numeric(self):
        with self.assertRaises(TypeError):
            polygon = Polygon(10, 30, 60, "100", 45, 45, 0, 40)
        polygon = Polygon(10, 30, 60, 100.5, 45, 45, 0, 40)


    def test_must_be_even_number_of_coordinate_values(self):
        with self.assertRaises(ValueError):
            polygon = Polygon(10, 30, 100, 45, 45, 0, 40)
