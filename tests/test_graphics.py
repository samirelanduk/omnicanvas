import unittest
import sys
sys.path.append(".")
from omnicanvas.graphics import *

class GraphicsUnitTest(unittest.TestCase):

    def check_valid_graphic(self, graphic):
        self.assertIsInstance(graphic.line_style, str)
        graphic.line_width + 1
        self.assertIsInstance(graphic.line_color, str)
        graphic.line_opacity + 0.1
        self.assertEqual(len(graphic.line_color), 7)
        graphic.rotate(0, 0, 45)


    def check_valid_shape(self, shape):
        self.check_valid_graphic(shape)
        if shape.fill_color is not None:
            self.assertIsInstance(shape.fill_color, str)
            self.assertEqual(len(shape.shape_color), 7)
        self.assertGreaterEqual(shape.opacity, 0)
        self.assertLessEqual(shape.opacity, 1)


    def check_valid_box(self, box):
        self.check_valid_shape(box)
        box.x + 1
        box.y + 1
        box.width + 1
        box.height + 1
        self.assertIsInstance(box.center(), tuple)
        self.assertEqual(len(box.center()), 2)
        self.assertGreaterEqual(box.center()[0], box.x)
        self.assertGreaterEqual(box.center()[1], box.y)



class TestLineGraphic(GraphicsUnitTest):

    def test_doesnt_need_keyword_arguments(self):
        line = Line(1, 1, 2, 2)
        self.check_valid_graphic(line)


    def test_will_accept_keywords(self):
        line = Line(1, 1, 2, 2, line_style="-", line_width=1, line_color="#000000")
        self.check_valid_graphic(line)


    def test_can_resize(self):
        line = Line(10, 10, 90, 90)
        line.scale(0.4, 3)
        self.assertEqual(line.x1, 4)
        self.assertEqual(line.y1, 30)
        self.assertEqual(line.x2, 36)
        self.assertEqual(line.y2, 270)


    def test_can_move(self):
        line = Line(10, 10, 90, 90)
        line.translate(20, 50)
        self.assertEqual(line.x1, 30)
        self.assertEqual(line.y1, 60)
        self.assertEqual(line.x2, 110)
        self.assertEqual(line.y2, 140)



class TestRectangleGraphic(GraphicsUnitTest):

    def test_can_create_rectangle(self):
        rectangle = Rectangle(1, 1, 10, 10)
        self.check_valid_box(rectangle)


    def test_can_resize(self):
        rectangle = Rectangle(1, 1, 10, 10)
        rectangle.scale(3, 0.25)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 0.25)
        self.assertEqual(rectangle.width, 30)
        self.assertEqual(rectangle.height, 2.5)


    def test_can_move(self):
        rectangle = Rectangle(1, 1, 10, 10)
        rectangle.translate(30, -25)
        self.assertEqual(rectangle.x, 31)
        self.assertEqual(rectangle.y, -24)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 10)



class TestPolylineGraphic(GraphicsUnitTest):

    def test_path_points_format_correctly(self):
        polyline = Polyline(10,10, 10,30, 34,45, 100,101, 19,200)
        self.check_valid_graphic(polyline)
        self.assertIsInstance(polyline.points, list)
        for point in polyline.points:
            self.assertIsInstance(point, tuple)
            self.assertEqual(len(point), 2)


    def test_cant_provide_odd_number_of_points(self):
        self.assertRaises(AssertionError, lambda: Polyline(1, 2, 3, 4, 5))


    def test_can_resize(self):
        polyline = Polyline(10,10, 10,30, 34,45, 100,101, 19,200)
        polyline.scale(8, 0.5)
        self.assertEqual(polyline.points, [(80,5),(80,15),(272,22.5),(800,50.5),(152,100)])


    def test_can_move(self):
        polyline = Polyline(10,10, 10,30, 34,45, 100,101, 19,200)
        polyline.translate(8, -200)
        self.assertEqual(polyline.points, [(18,-190),(18,-170),(42,-155),(108,-99),(27,0)])



class TestPolygonGraphic(GraphicsUnitTest):

    def test_path_points_format_correctly(self):
        polygon = Polygon(10,10, 10,30, 34,45, 100,101, 19,200)
        self.check_valid_shape(polygon)
        self.assertIsInstance(polygon.points, list)
        for point in polygon.points:
            self.assertIsInstance(point, tuple)
            self.assertEqual(len(point), 2)



class TestCircleGraphic(GraphicsUnitTest):

    def test_can_create_oval(self):
        oval = Oval(10, 10, 40, 80)
        self.check_valid_box(oval)
        self.check_valid_shape(oval)


class TestArcGraphic(GraphicsUnitTest):

    def test_can_create_arc(self):
        arc = Arc(10, 10, 30, 30, start_angle=45, end_angle=290)


    def test_cant_use_angles_over_360(self):
        self.assertRaises(AssertionError, lambda: Arc(1,1,3,3,start_angle=450, end_angle=290))
        self.assertRaises(AssertionError, lambda: Arc(1,1,3,3,start_angle=30, end_angle=390))


    def test_angle_less_than_360(self):
        arc = Arc(10, 10, 40, 80, start_angle=35, end_angle=25)
        self.assertLess(arc.angle(), 360)
        self.assertEqual(arc.angle(), 350)


    def test_angle_greater_than_360(self):
        arc = Arc(10, 10, 40, 80, start_angle=25, end_angle=35)
        self.assertGreaterEqual(arc.angle(), 0)



class TestTextGraphic(GraphicsUnitTest):

    def test_can_create_text(self):
        text = Text(20, 30, "Test")
        self.check_valid_graphic(text)


    def test_can_resize(self):
        text = Text(20, 30, "Test")
        text.scale(4, 4)
        self.assertEqual(text.x, 80)
        self.assertEqual(text.y, 120)


    def test_can_move(self):
        text = Text(20, 30, "Test")
        text.translate(4, 4)
        self.assertEqual(text.x, 24)
        self.assertEqual(text.y, 34)




class TestValidRepr(GraphicsUnitTest):

    def test_reprs_ok(self):
        line = Line(1,1,2,2)
        polyline = Polyline(1,1,2,2,3,3)
        rectangle = Rectangle(1,1,2,2)
        polygon = Polygon(1,1,2,2,3,3,4,4)
        oval = Oval(1,1,2,2)
        arc = Arc(10, 10, 40, 80, start_angle=35, end_angle=25)
        text = Text(20, 30, "Test")

        self.assertRegex(line.__repr__(), r"<Line object: (.+,.+) to (.+,.+)>")
        self.assertRegex(polyline.__repr__(), r"<Polyline object: .+ points>")
        self.assertRegex(rectangle.__repr__(), r"<.+ × .+ Rectangle object at (.+,.+)>")
        self.assertRegex(polygon.__repr__(), r"<Polygon object: .+ vertices>")
        self.assertRegex(oval.__repr__(), r"<.+ × .+ Oval object centered at (.+,.+)>")
        self.assertRegex(arc.__repr__(), r"<.+ × .+ .+ Arc object at (.+,.+)>")
        self.assertRegex(text.__repr__(), r'<".+" Text object at (.+,.+)>')



if __name__ == "__main__":
    unittest.main()
