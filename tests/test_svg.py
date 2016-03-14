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



if __name__ == "__main__":
    unittest.main()
