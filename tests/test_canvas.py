import unittest
import sys
sys.path.append(".")
from omnicanvas import *

class TestCanvas(unittest.TestCase):

    def test_can_resize_canvas(self):
        canvas = Canvas(width=600, height=400)

        oval = canvas.draw_oval(30, 40, 120, 200)
        line = canvas.draw_line(90, 90, 500, 300)

        canvas.resize(width=400, height=800)

        self.assertEqual(oval.x, 20)
        self.assertEqual(oval.y, 80)
        self.assertEqual(oval.width, 80)
        self.assertEqual(oval.height, 400)
        self.assertEqual(line.x1, 60)
        self.assertEqual(line.y1, 180)
        self.assertEqual(line.x2, 1000/3)
        self.assertEqual(line.y2, 600)



if __name__ == "__main__":
    unittest.main()
