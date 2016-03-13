import unittest
import sys
sys.path.append(".")
from omnicanvas.graphics import *
from omnicanvas.svg import *

class TestGraphicsCanProduceSvg(unittest.TestCase):

    def test_lines_can_produce_svg(self):
        line = Line(10, 10, 90, 90, line_width=5, line_style="--", line_color="#FF0000")
        svg = line.to_svg()



if __name__ == "__main__":
    unittest.main()
