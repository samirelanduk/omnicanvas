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


    def test_polyline_coordinates_must_be_numeric(self):
        with self.assertRaises(TypeError):
            Polyline(10, 30, 60, "100", 45, 45, 0, 40)
        Polyline(10, 30, 60, 100.5, 45, 45, 0, 40)


    def test_must_be_even_number_of_coordinate_values(self):
        with self.assertRaises(ValueError):
            Polyline(10, 30, 100, 45, 45, 0, 40)


    def test_must_be_at_least_two_vertices(self):
        with self.assertRaises(GeometryError):
            Polyline(45, 45)



class PolylinePropertiesTests(TestCase):

    def test_basic_properties(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(polyline.coordinates(), polyline._coordinates)


    def test_coordinates_are_read_only(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45, 0, 40)
        polyline.coordinates().append(70)
        self.assertEqual(polyline.coordinates(), [10, 30, 60, 100, 45, 45, 0, 40])


    def test_can_add_polyline_vertex(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45)
        polyline.add_vertex(0, 40)
        self.assertEqual(polyline.coordinates(), [10, 30, 60, 100, 45, 45, 0, 40])


    def test_added_vertices_must_be_numeric(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45)
        with self.assertRaises(TypeError):
            polyline.add_vertex("0", 40)
        with self.assertRaises(TypeError):
            polyline.add_vertex(0, "40")
        polyline.add_vertex(0.3, 40.7)


    def test_can_remove_vertex_from_polyline(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45, 0, 40, 34, 43)
        polyline.remove_vertex(0)
        self.assertEqual(polyline.coordinates(), [60, 100, 45, 45, 0, 40, 34, 43])
        polyline.remove_vertex(2)
        self.assertEqual(polyline.coordinates(), [60, 100, 45, 45, 34, 43])


    def test_vertex_index_must_be_int(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45, 0, 40)
        with self.assertRaises(TypeError):
            polyline.remove_vertex(0.5)


    def test_cannot_reduce_number_of_vertices_below_two(self):
        polyline = Polyline(10, 30, 60, 100)
        with self.assertRaises(GeometryError):
            polyline.remove_vertex(1)


    def test_can_get_coordinates_as_coordinate_tuples(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(
         polyline.coordinates(xy_pairs=True),
         ((10, 30), (60, 100), (45, 45), (0, 40))
        )



class SvgTests(TestCase):

    def test_can_make_basic_svg(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45, 0, 40)
        self.assertEqual(
         polyline.to_svg(),
         '<polyline points="10.0,30.0, 60.0,100.0, 45.0,45.0, 0.0,40.0"'
         ' style="stroke:#000000;" />'
        )


    def test_can_create_rotated_polyline_svg(self):
        polyline = Polyline(10, 30, 60, 100, 45, 45, 0, 40, rotation=(200, 200, 45))
        self.assertEqual(
         polyline.to_svg(),
         '<polyline points="10.0,30.0, 60.0,100.0, 45.0,45.0, 0.0,40.0"'
         ' style="stroke:#000000;" transform="rotate(45.0 200.0 200.0)" />'
        )


    def test_data_in_polyline_svg(self):
        polyline = Polyline(
         10, 30, 60, 100, 45, 45, 0, 40, data={"onclick":"func(true);", "a": "b"}
        )
        self.assertIn(
         'onclick="func(true);"',
         polyline.to_svg()
        )
        self.assertIn(
         'a="b"',
         polyline.to_svg()
        )
