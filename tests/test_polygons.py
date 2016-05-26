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
        self.assertEqual(polygon.rotation, (0, 0, 0))
        self.assertEqual(str(polygon), "<Polygon (4 points)>")


    def test_polygon_coordinates_must_be_numeric(self):
        with self.assertRaises(TypeError):
            polygon = Polygon(10, 30, 60, "100", 45, 45, 0, 40)
        polygon = Polygon(10, 30, 60, 100.5, 45, 45, 0, 40)


    def test_must_be_even_number_of_coordinate_values(self):
        with self.assertRaises(ValueError):
            polygon = Polygon(10, 30, 100, 45, 45, 0, 40)



class PointsTests(TestCase):

    def test_can_turn_points_into_coordinate_tuple(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(
         polygon.coordinates_to_xy_pairs(),
         ((10, 30), (60, 100), (45, 45), (0, 40))
        )


    def test_coordinate_generation_warns_about_odd_number_of_coordinates(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        polygon.coordinates.pop()
        with self.assertRaises(ValueError):
             polygon.coordinates_to_xy_pairs()



class SvgTests(TestCase):

    def test_can_make_basic_svg(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(
         polygon.to_svg(),
         '<polygon points="10.0,30.0, 60.0,100.0, 45.0,45.0, 0.0,40.0"'
         ' style="fill:#FFFFFF;stroke:#000000;" />'
        )
