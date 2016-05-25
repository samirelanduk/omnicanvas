from unittest import TestCase
from omnicanvas.canvas import Canvas
import omnicanvas.graphics as graphics

class CanvasCreationTests(TestCase):

    def test_can_create_canvas(self):
        canvas = Canvas(700, 500)
        self.assertEqual(canvas.graphics, [])
        self.assertEqual(canvas.width, 700)
        self.assertEqual(canvas.height, 500)
        self.assertEqual(canvas.background_color, None)
        self.assertEqual(canvas.border_width, 0)
        self.assertEqual(canvas.border_style, "-")
        self.assertEqual(canvas.border_color, "#000000")
        self.assertEqual(
         str(canvas),
         "<Canvas 700×500 (0 Graphics)>"
        )


    def test_dimensions_must_be_numeric(self):
        with self.assertRaises(TypeError):
            Canvas("700", 500)
        with self.assertRaises(TypeError):
            Canvas(700, "500")
        with self.assertRaises(TypeError):
            Canvas("700", "500")


    def test_float_dimensions_converted_to_int(self):
        canvas = Canvas(100.0, 200)
        self.assertEqual(canvas.width, 100)
        self.assertIsInstance(canvas.width, int)
        canvas = Canvas(100.1, 200)
        self.assertEqual(canvas.width, 100)
        canvas = Canvas(100.6, 200)
        self.assertEqual(canvas.width, 101)
        canvas = Canvas(100, 200.0)
        self.assertEqual(canvas.height, 200)
        self.assertIsInstance(canvas.height, int)
        canvas = Canvas(100, 200.1)
        self.assertEqual(canvas.height, 200)
        canvas = Canvas(100, 200.6)
        self.assertEqual(canvas.height, 201)


    def test_can_create_canvas_with_background_color(self):
        canvas = Canvas(700, 500, background_color="#FFFF00")
        self.assertEqual(canvas.background_color, "#FFFF00")


    def test_canvas_creation_will_capitalise_color(self):
        canvas = Canvas(700, 500, background_color="#ffff00")
        self.assertEqual(canvas.background_color, "#FFFF00")


    def test_canvas_color_must_be_str(self):
        with self.assertRaises(TypeError):
            canvas = Canvas(700, 500, background_color=999944)
        canvas = Canvas(700, 500, background_color=None)
        self.assertIs(canvas.background_color, None)


    def test_canvas_color_must_be_formatted_correctly(self):
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, background_color="FFFF00")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, background_color="#FFF00")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, background_color="#FF0")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, background_color="#FFFG00")


    def test_can_create_canvas_with_border_width(self):
        canvas = Canvas(700, 500, border_width=2.5)
        self.assertEqual(canvas.border_width, 2.5)


    def test_canvas_border_width_must_be_numeric(self):
        with self.assertRaises(TypeError):
            canvas = Canvas(700, 500, border_width=None)
        with self.assertRaises(TypeError):
            canvas = Canvas(700, 500, border_width="1")
        canvas = Canvas(700, 500, border_width=2.5)
        canvas = Canvas(700, 500, border_width=2)


    def test_can_create_canvas_with_border_style(self):
        canvas = Canvas(700, 500, border_style="--")
        self.assertEqual(canvas.border_style, "--")


    def test_canvas_border_style_must_be_str(self):
        with self.assertRaises(TypeError):
            canvas = Canvas(700, 500, border_style=(1,1))
        with self.assertRaises(TypeError):
            canvas = Canvas(700, 500, border_style=None)


    def test_canvas_border_style_must_be_valid(self):
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, border_style="")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, border_style="888")


    def test_can_create_canvas_with_border_color(self):
        canvas = Canvas(700, 500, border_color="#FF0000")
        self.assertEqual(canvas.border_color, "#FF0000")


    def test_canvas_border_will_capitalise_color(self):
        canvas = Canvas(700, 500, border_color="#ffff00")
        self.assertEqual(canvas.border_color, "#FFFF00")


    def test_canvas_border_color_must_be_str(self):
        with self.assertRaises(TypeError):
            canvas = Canvas(700, 500, border_color=999944)
        with self.assertRaises(TypeError):
            canvas = Canvas(700, 500, border_color=None)


    def test_canvas_border_color_must_be_formatted_correctly(self):
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, border_color="FFFF00")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, border_color="#FFF00")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, border_color="#FF0")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, border_color="#FFFG00")



class GraphicAdditionTests(TestCase):

    def setUp(self):
        self.canvas = Canvas(400, 400)


    def test_can_add_rectangle(self):
        self.canvas.add_rectangle(10, 10, 50, 100)
        self.assertIsInstance(
         self.canvas.graphics[-1],
         graphics.Rectangle
        )
        self.assertEqual(self.canvas.graphics[-1].width, 50)
        self.assertEqual(self.canvas.graphics[-1].height, 100)
        self.canvas.add_rectangle(10, 10, 50, 100, opacity=0.3, line_style="..")
        self.assertEqual(len(self.canvas.graphics), 2)
        self.assertEqual(self.canvas.graphics[-1].opacity, 0.3)
        self.assertEqual(self.canvas.graphics[-1].line_style, "..")
        self.assertEqual(self.canvas.graphics[-1].line_width, 1)


    def test_can_add_line(self):
        self.canvas.add_line(10, 10, 50, 100)
        self.assertIsInstance(
         self.canvas.graphics[-1],
         graphics.Line
        )
        self.assertEqual(self.canvas.graphics[-1].x1, 10)
        self.assertEqual(self.canvas.graphics[-1].y2, 100)
        self.canvas.add_line(10, 10, 50, 100, line_color="#999999", line_style="..")
        self.assertEqual(len(self.canvas.graphics), 2)
        self.assertEqual(self.canvas.graphics[-1].line_color, "#999999")
        self.assertEqual(self.canvas.graphics[-1].line_style, "..")
        self.assertEqual(self.canvas.graphics[-1].line_width, 1)


    def test_can_add_polygon(self):
        self.canvas.add_polygon(10, 30, 100, 45, 45, 40)
        self.assertIsInstance(
         self.canvas.graphics[-1],
         graphics.Polygon
        )
        self.assertEqual(self.canvas.graphics[-1].coordinates[-1], 40)
        self.canvas.add_polygon(10, 30, 100, 45, 45, 40, opacity=0.1)
        self.assertEqual(len(self.canvas.graphics), 2)
        self.assertEqual(self.canvas.graphics[-1].opacity, 0.1)
        self.assertEqual(self.canvas.graphics[-1].line_width, 1)


    def test_can_add_text(self):
        self.canvas.add_text(10, 30, "TEXT")
        self.assertIsInstance(
         self.canvas.graphics[-1],
         graphics.Text
        )
        self.assertEqual(self.canvas.graphics[-1].text, "TEXT")
        self.canvas.add_text(10, 30, "TEXT", vertical_align="top")
        self.assertEqual(len(self.canvas.graphics), 2)
        self.assertEqual(self.canvas.graphics[-1].vertical_align, "top")
        self.assertEqual(self.canvas.graphics[-1].opacity, 1)
        self.assertEqual(self.canvas.graphics[-1].line_width, 0)



class CanvasSvgTests(TestCase):

    def test_can_make_shell_svg(self):
        canvas = Canvas(300, 200)
        self.assertEqual(
         canvas.to_svg(),
         '<svg width="300" height="200">\n\n</svg>'
        )


    def test_canvas_svg_contains_graphic_svg(self):
        canvas = Canvas(300, 200)
        canvas.add_line(0, 0, 300, 200)
        self.assertEqual(
         canvas.to_svg(),
         "\n".join((
          '<svg width="300" height="200">',
          canvas.graphics[0].to_svg(),
          "</svg>"
         ))
        )
