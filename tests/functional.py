import unittest
import sys
sys.path.append(".")
import omnicanvas

class ProduceSvg(unittest.TestCase):

    def setUp(self):
        pass


    def test_can_make_svg_file(self):
        # User creates a canvas
        canvas = omnicanvas.Canvas(width=700, height=700, background_color="#11BB11")

        # User draws on the canvas
        canvas.draw_line(10, 10, 100, 100, line_color="#0000FF")
        canvas.draw_line(
         canvas.width() - 10, canvas.height() - 10,
         canvas.width() - 100, canvas.width() - 100,
         line_color="#0000FF"
        )
        canvas.draw_oval(
         canvas.width() * 0.3, canvas.height() * 0.3,
         canvas.width() * 0.7, canvas.height() * 0.7,
         fill_color="#FF0000"
        )

        # User resizes the canvas
        canvas.resize(width=900, height=600)

        # User saves as SVG
        canvas.save("svg", "test_can_make_svg_file.svg")


if __name__ == "__main__":
    unittest.main()
