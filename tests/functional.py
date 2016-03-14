import unittest
import sys
sys.path.append(".")
import omnicanvas
import math

class ProduceSvg(unittest.TestCase):

    def setUp(self):
        self.canvas = omnicanvas.Canvas(
         width=700, height=700, background_color="#F0F0F0"
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


    def test_can_make_rectangle_svg_file(self):
        for n in range(7):
            self.canvas.draw_rectangle(
             (n + 1) * self.canvas.width() / 14,
             (n + 1) * self.canvas.height() / 14,
             self.canvas.width() * (0.5 - (n / 50)),
             self.canvas.height() * (0.5 - (n / 50)),
             line_style="..",
             line_width=2.5,
             line_color="#%02xFF%02x" % (int(255 * (n/6)), int(255 * ((6-n)/6))),
             opacity=0.5,
             fill_color="#%02xFF%02x" % (int(255 * ((6-n)/6)), int(255 * (n/6)))
            )
        self.canvas.save("svg", "rectangle_test.svg")


    def test_can_make_polygon_svg(self):
        points = (
         {"x": self.canvas.width() / 2, "y": self.canvas.height() * 0.3},
         {"x": self.canvas.width() / 2, "y": self.canvas.height() * 0.7}
        )
        for _ in range(6):
            delta_x = points[1]["x"] - points[0]["x"]
            delta_y = points[1]["y"] - points[0]["y"]
            gradient = (delta_y / delta_x) if delta_x else math.inf
            inverse_gradient = gradient
            if gradient:
                inverse_gradient = 1 / gradient
            elif gradient == 0:
                inverse_gradient = math.inf
            else:
                inverse_gradient = 0
            angle = math.atan(inverse_gradient)
            delta_y = math.sin(angle) * (self.canvas.width() * 0.075)
            delta_x = math.cos(angle) * (self.canvas.width() * 0.075)
            points = points + ({"x": points[0]["x"] - delta_x, "y": points[0]["y"] + delta_y},)
            self.canvas.draw_polygon(
             points[0]["x"], points[0]["y"],
             points[1]["x"], points[1]["y"],
             points[2]["x"], points[2]["y"],
             line_width=2,
             opacity=0.4,
             fill_color="#FF6666",
             line_color="#0000FF"
            )
            points = (points[2], points[1])
        self.canvas.save("svg", "polygon_test.svg")


    def test_can_make_oval_svg(self):
        for n in range(7):
            self.canvas.draw_oval(
             (n + 1) * (self.canvas.width() / 14),
             (n + 1) * self.canvas.height() / 14,
             100 + (n * 10), #self.canvas.width() * (0.5 + (n / 50)),
             170 - (n * 10), #self.canvas.height() * (1 - (0.5 + (n / 50))),
             line_style="..",
             line_width=2.5,
             line_color="#%02xFF%02x" % (int(255 * (n/6)), int(255 * ((6-n)/6))),
             opacity=0.5,
             fill_color="#%02xFF%02x" % (int(255 * ((6-n)/6)), int(255 * (n/6)))
            )
        self.canvas.save("svg", "oval_test.svg")




if __name__ == "__main__":
    unittest.main()
