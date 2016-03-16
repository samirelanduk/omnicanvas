import unittest
import sys
sys.path.append(".")
from omnicanvas.graphics import *
from omnicanvas.svg import *

class TestGraphicsCanProduceSvg(unittest.TestCase):

    def test_lines_can_produce_svg(self):
        line = Line(10, 10, 90, 90, line_width=5, line_style="--", line_color="#FF0000")
        svg = line.to_svg()


    def test_polylines_can_produce_svg(self):
        polyline = Polyline(
         10, 10, 90, 90, 100, 100, line_width=0.5, line_style="..", line_color="#00FF00"
        )
        svg = polyline.to_svg()


    def test_rectangles_can_produce_svg(self):
        rectangle = Rectangle(
         10, 10, 90, 90, line_width=15, line_style="-", line_color="#0000FF"
        )
        svg = rectangle.to_svg()


    def test_polygons_can_produce_svg(self):
        polygon = Polygon(
         10, 10, 90, 90, 100, 100, line_width=0.5, line_style="..", line_color="#00FF00", fill_color="#999999"
        )
        svg = polygon.to_svg()


    def test_ovals_can_produce_svg(self):
        oval = Oval(
         10, 10, 90, 90, line_width=15, line_style="-", line_color="#0000FF"
        )
        svg = oval.to_svg()


    def test_arc_can_produce_svg(self):
        arc = Arc(
         10, 10, 90, 90, start_angle=90, end_angle=260, line_width=15, line_style="-", line_color="#0000FF"
        )
        svg = arc.to_svg()


    def test_text_can_produce_svg(self):
        text = Text(
         10, 10, "test", color="#377899", font_size=98
        )
        svg = text.to_svg()



class TestSvgHelpers(unittest.TestCase):

    def test_can_find_points(self):
        self.assertAlmostEqual(
         get_point_from_angle(100, 100, 200, 150, 0)[0],
         200,
         delta=0.001
        )
        self.assertAlmostEqual(
         get_point_from_angle(100, 100, 200, 150, 0)[1],
         100,
         delta=0.001
        )
        self.assertAlmostEqual(
         get_point_from_angle(100, 100, 200, 150, 90)[0],
         100,
         delta=0.001
        )
        self.assertAlmostEqual(
         get_point_from_angle(100, 100, 200, 150, 90)[1],
         25,
         delta=0.001
        )
        self.assertAlmostEqual(
         get_point_from_angle(100, 100, 200, 150, 180)[0],
         0,
         delta=0.001
        )
        self.assertAlmostEqual(
         get_point_from_angle(100, 100, 200, 150, 180)[1],
         100,
         delta=0.001
        )
        self.assertAlmostEqual(
         get_point_from_angle(100, 100, 200, 150, 270)[0],
         100,
         delta=0.001
        )
        self.assertAlmostEqual(
         get_point_from_angle(100, 100, 200, 150, 270)[1],
         175,
         delta=0.001
        )


if __name__ == "__main__":
    unittest.main()
