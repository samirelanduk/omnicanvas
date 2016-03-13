import unittest
import sys
sys.path.append(".")
import omnicanvas

class ProduceSvg(unittest.TestCase):

    def setUp(self):
        self.canvas = omnicanvas.Canvas(
         width=700, height=700, background_color="#11BB11"
        )
        self.make_grid(self.canvas)


    def make_grid(self, canvas):
        for n in range(11):
            canvas.draw_line(
             n * (canvas.width() / 10), 0,
             n * (canvas.width() / 10), canvas.height()
            )
            canvas.draw_line(
             0, n * (canvas.height() / 10),
             canvas.width(), n * (canvas.height() / 10)
            )


    def test_can_make_line_svg_file(self):
        self.canvas.draw_line(
         self.canvas.width() * 0.05, self.canvas.height() * 0.05,
         self.canvas.width() * 0.95, self.canvas.height() * 0.05,
         line_style="--",
         line_width=1,
         line_color="#FF0000"
        )
        self.canvas.draw_line(
         self.canvas.width() * 0.05, self.canvas.height() * 0.15,
         self.canvas.width() * 0.85, self.canvas.height() * 0.25,
         line_style="--",
         line_width=2,
         line_color="#00FF00"
        )
        self.canvas.draw_line(
         self.canvas.width() * 0.05, self.canvas.height() * 0.25,
         self.canvas.width() * 0.75, self.canvas.height() * 0.45,
         line_style="-",
         line_width=3,
         line_color="#0000FF"
        )
        self.canvas.draw_line(
         self.canvas.width() * 0.15, self.canvas.height() * 0.95,
         self.canvas.width() * 0.15, self.canvas.height() * 0.5,
         line_style="-",
         line_width=5,
         line_color="#FF00FF"
        )
        self.canvas.draw_line(
         self.canvas.width() * 0.25, self.canvas.height() * 0.95,
         self.canvas.width() * 0.25, self.canvas.height() * 0.7,
         line_style="..",
         line_width=3,
         line_color="#FFFF00"
        )
        self.canvas.draw_line(
         self.canvas.width() * 0.35, self.canvas.height() * 0.95,
         self.canvas.width() * 0.35, self.canvas.height() * 0.9,
         line_style="-",
         line_width=1,
         line_color="#00FFFF"
        )
        self.canvas.save("svg", "line_test.svg")


    def test_can_make_polyline_svg_file(self):
        self.canvas.draw_polyline(
         50, 50, 400, 50, 690, 85, 70, 630,
         line_style="--",
         line_width=2,
         line_color="#34944D"
        )
        self.canvas.save("svg", "polyline_test.svg")


if __name__ == "__main__":
    unittest.main()
