import unittest
import sys
sys.path.append(".")
import omnicanvas

class ProduceSvg(unittest.TestCase):

    def setUp(self):
        pass


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


    def test_can_make_svg_file(self):
        canvas = omnicanvas.Canvas(width=700, height=700, background_color="#11BB11")

        self.make_grid(canvas)
        canvas.draw_line(
         canvas.width() * 0.05, canvas.height() * 0.05,
         canvas.width() * 0.95, canvas.height() * 0.05,
         line_style="--",
         line_width=1,
         line_color="#FF0000"
        )
        canvas.draw_line(
         canvas.width() * 0.05, canvas.height() * 0.15,
         canvas.width() * 0.85, canvas.height() * 0.25,
         line_style="--",
         line_width=2,
         line_color="#00FF00"
        )
        canvas.draw_line(
         canvas.width() * 0.05, canvas.height() * 0.25,
         canvas.width() * 0.75, canvas.height() * 0.45,
         line_style="-",
         line_width=3,
         line_color="#0000FF"
        )
        canvas.draw_line(
         canvas.width() * 0.15, canvas.height() * 0.95,
         canvas.width() * 0.15, canvas.height() * 0.5,
         line_style="-",
         line_width=5,
         line_color="#FF00FF"
        )
        canvas.draw_line(
         canvas.width() * 0.25, canvas.height() * 0.95,
         canvas.width() * 0.25, canvas.height() * 0.7,
         line_style="..",
         line_width=3,
         line_color="#FFFF00"
        )
        canvas.draw_line(
         canvas.width() * 0.35, canvas.height() * 0.95,
         canvas.width() * 0.35, canvas.height() * 0.9,
         line_style="-",
         line_width=1,
         line_color="#00FFFF"
        )

        canvas.save("svg", "line_test.svg")


if __name__ == "__main__":
    unittest.main()
