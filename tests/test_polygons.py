from unittest import TestCase
from omnicanvas.graphics import ShapeGraphic, Polygon
from omnicanvas.exceptions import GeometryError

class PolygonCreationTests(TestCase):

    def test_can_create_polyon(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertIsInstance(polygon, ShapeGraphic)
        self.assertEqual(polygon._coordinates, [10, 30, 60, 100, 45, 45, 0, 40])
        self.assertEqual(polygon._fill_color, "#FFFFFF")
        self.assertEqual(polygon._opacity, 1)
        self.assertEqual(polygon._line_width, 1)
        self.assertEqual(polygon._line_style, "-")
        self.assertEqual(polygon._line_color, "#000000")
        self.assertEqual(polygon._rotation, (0, 0, 0))
        self.assertEqual(polygon._data, {})


    def test_polygon_repr(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(str(polygon), "<Polygon (4 points)>")


    def test_polygon_coordinates_must_be_numeric(self):
        with self.assertRaises(TypeError):
            Polygon(10, 30, 60, "100", 45, 45, 0, 40)
        Polygon(10, 30, 60, 100.5, 45, 45, 0, 40)


    def test_must_be_even_number_of_coordinate_values(self):
        with self.assertRaises(ValueError):
            Polygon(10, 30, 100, 45, 45, 0, 40)


    def test_must_be_at_least_three_vertices(self):
        with self.assertRaises(GeometryError):
            Polygon(45, 45, 0, 40)



class PolygonPropertiesTests(TestCase):

    def test_basic_properties(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(polygon.coordinates(), tuple(polygon._coordinates))


    def test_can_add_polygon_vertex(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45)
        polygon.add_vertex(0, 40)
        self.assertEqual(polygon.coordinates(), (10, 30, 60, 100, 45, 45, 0, 40))


    def test_added_vertices_must_be_numeric(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45)
        with self.assertRaises(TypeError):
            polygon.add_vertex("0", 40)
        with self.assertRaises(TypeError):
            polygon.add_vertex(0, "40")
        polygon.add_vertex(0.3, 40.7)


    def test_can_remove_vertex_from_polygon(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40, 34, 43)
        polygon.remove_vertex(0)
        self.assertEqual(polygon.coordinates(), (60, 100, 45, 45, 0, 40, 34, 43))
        polygon.remove_vertex(2)
        self.assertEqual(polygon.coordinates(), (60, 100, 45, 45, 34, 43))


    def test_vertex_index_must_be_int(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        with self.assertRaises(TypeError):
            polygon.remove_vertex(0.5)


    def test_cannot_reduce_number_of_vertices_below_three(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45)
        with self.assertRaises(GeometryError):
            polygon.remove_vertex(1)


    def test_can_get_coordinates_as_coordinate_tuples(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(
         polygon.coordinates(xy_pairs=True),
         ((10, 30), (60, 100), (45, 45), (0, 40))
        )



class SvgTests(TestCase):

    def test_can_make_basic_svg(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(
         polygon.to_svg(),
         '<polygon points="10.0,30.0, 60.0,100.0, 45.0,45.0, 0.0,40.0"'
         ' style="fill:#FFFFFF;stroke:#000000;" />'
        )


    def test_can_create_rotated_polygon_svg(self):
        polygon = Polygon(10, 30, 60, 100, 45, 45, 0, 40, rotation=(200, 200, 45))
        self.assertEqual(
         polygon.to_svg(),
         '<polygon points="10.0,30.0, 60.0,100.0, 45.0,45.0, 0.0,40.0"'
         ' style="fill:#FFFFFF;stroke:#000000;" transform="rotate(45.0 200.0 200.0)" />'
        )


    def test_data_in_polygon_svg(self):
        polygon = Polygon(
         10, 30, 60, 100, 45, 45, 0, 40, data={"onclick":"func(true);", "a": "b"}
        )
        self.assertIn(
         'onclick="func(true);"',
         polygon.to_svg()
        )
        self.assertIn(
         'a="b"',
         polygon.to_svg()
        )
