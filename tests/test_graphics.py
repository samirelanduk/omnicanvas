import unittest
import sys
sys.path.append(".")
from omnicanvas.graphics import *

class GraphicsUnitTest(unittest.TestCase):

    def check_valid_box(self, box):
        box.x + 1
        box.y + 1
        box.width + 1
        box.height + 1


    def check_valid_line(self, line):
        self.assertIsInstance(line.line_style, str)
        self.assertIsInstance(line.line_width, int)
        self.assertIsInstance(line.line_color, str)
        self.assertEqual(len(line.line_color), 7)


    def check_valid_shape(self, shape):
        self.check_valid_line(shape)
        if shape.fill_color is not None:
            self.assertIsInstance(shape.fill_color, str)
            self.assertEqual(len(shape.shape_color), 7)
        self.assertGreaterEqual(shape.opacity, 0)
        self.assertLessEqual(shape.opacity, 1)



class TestLineGraphic(GraphicsUnitTest):

    def test_doesnt_need_keyword_arguments(self):
        line = Line(1, 1, 2, 2)
        self.check_valid_line(line)


    def test_will_accept_keywords(self):
        line = Line(1, 1, 2, 2, line_style="-", line_width=1, line_color="#000000")
        self.check_valid_line(line)



class TestPathGraphic(GraphicsUnitTest):

    def test_path_points_format_correctly(self):
        path = Path(10,10, 10,30, 34,45, 100,101, 19,200)
        self.check_valid_line(path)
        self.assertIsInstance(path.points, list)
        for point in path.points:
            self.assertIsInstance(point, tuple)
            self.assertEqual(len(point), 2)


    def test_cant_provide_odd_number_of_points(self):
        self.assertRaises(AssertionError, lambda: Path(1, 2, 3, 4, 5))



class TestRectangleGraphic(GraphicsUnitTest):

    def test_can_create_rectangle(self):
        rectangle = Rectangle(1, 1, 10, 10)
        self.check_valid_box(rectangle)
        self.check_valid_shape(rectangle)



class TestPolygonGraphic(GraphicsUnitTest):

    def test_path_points_format_correctly(self):
        polygon = Polygon(10,10, 10,30, 34,45, 100,101, 19,200)
        self.check_valid_shape(polygon)
        self.assertIsInstance(polygon.points, list)
        for point in polygon.points:
            self.assertIsInstance(point, tuple)
            self.assertEqual(len(point), 2)



class TestValidRepr(GraphicsUnitTest):

    def test_reprs_ok(self):
        line = Line(1,1,2,2)
        path = Path(1,1,2,2,3,3)
        rectangle = Rectangle(1,1,2,2)
        polygon = Polygon(1,1,2,2,3,3,4,4)

        self.assertRegex(line.__repr__(), r"<Line object: (.+,.+) to (.+,.+)>")
        self.assertRegex(path.__repr__(), r"<Path object: .+ points>")
        self.assertRegex(rectangle.__repr__(), r"<.+ × .+ Rectangle object at (.+,.+)>")
        self.assertRegex(polygon.__repr__(), r"<Polygon object: .+ vertices>")



if __name__ == "__main__":
    unittest.main()
