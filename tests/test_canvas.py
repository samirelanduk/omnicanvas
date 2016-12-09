import os
from unittest import TestCase
from omnicanvas.canvas import Canvas
import omnicanvas.graphics as graphics

class CanvasCreationTests(TestCase):

    def test_can_create_canvas(self):
        canvas = Canvas(700, 500)
        self.assertEqual(canvas._graphics, [])
        self.assertEqual(canvas._width, 700)
        self.assertEqual(canvas._height, 500)
        self.assertEqual(canvas._background_color, None)


    def test_canvas_repr(self):
        canvas = Canvas(700, 500)
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
        self.assertEqual(canvas._width, 100)
        self.assertIsInstance(canvas._width, int)
        canvas = Canvas(100.1, 200)
        self.assertEqual(canvas._width, 100)
        canvas = Canvas(100.6, 200)
        self.assertEqual(canvas._width, 101)
        canvas = Canvas(100, 200.0)
        self.assertEqual(canvas._height, 200)
        self.assertIsInstance(canvas._height, int)
        canvas = Canvas(100, 200.1)
        self.assertEqual(canvas._height, 200)
        canvas = Canvas(100, 200.6)
        self.assertEqual(canvas._height, 201)


    def test_can_create_canvas_with_background_color(self):
        canvas = Canvas(700, 500, background_color="#FFFF00")
        self.assertEqual(canvas._background_color, "#FFFF00")


    def test_canvas_creation_will_capitalise_color(self):
        canvas = Canvas(700, 500, background_color="#ffff00")
        self.assertEqual(canvas._background_color, "#FFFF00")


    def test_canvas_color_must_be_str(self):
        with self.assertRaises(TypeError):
            canvas = Canvas(700, 500, background_color=999944)
        canvas = Canvas(700, 500, background_color=None)
        self.assertIs(canvas._background_color, None)


    def test_canvas_color_must_be_formatted_correctly(self):
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, background_color="FFFF00")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, background_color="#FFF00")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, background_color="#FF0")
        with self.assertRaises(ValueError):
            canvas = Canvas(700, 500, background_color="#FFFG00")



class CanvasPropertyTests(TestCase):

    def test_basic_propertie(self):
        canvas = Canvas(700, 500, background_color="#FFFF00")
        self.assertIs(canvas.width(), canvas._width)
        self.assertIs(canvas.height(), canvas._height)
        self.assertIs(canvas.background_color(), canvas._background_color)
        self.assertIs(canvas.graphics(), canvas._graphics)


    def test_can_set_dimensions(self):
        canvas = Canvas(700, 500)
        canvas.width(600)
        self.assertEqual(canvas.width(), 600)
        canvas.height(800)
        self.assertEqual(canvas.height(), 800)


    def test_dimensions_must_be_numeric(self):
        canvas = Canvas(700, 500)
        with self.assertRaises(TypeError):
            canvas.width("100")
        with self.assertRaises(TypeError):
            canvas.height("500")


    def test_float_dimensions_converted_to_int(self):
        canvas = Canvas(700, 500)
        canvas.width(600.0)
        self.assertEqual(canvas._width, 600)
        self.assertIsInstance(canvas._width, int)
        canvas.width(100.1)
        self.assertEqual(canvas._width, 100)
        canvas.height(600.0)
        self.assertEqual(canvas._height, 600)
        self.assertIsInstance(canvas._height, int)
        canvas.height(100.1)
        self.assertEqual(canvas._height, 100)


    def test_can_set_background_color(self):
        canvas = Canvas(700, 500)
        canvas.background_color("#FFFFFF")
        self.assertEqual(canvas.background_color(), "#FFFFFF")
        canvas.background_color("#787878")
        self.assertEqual(canvas.background_color(), "#787878")


    def test_setting_lowercase_color_will_capitalise(self):
        canvas = Canvas(700, 500)
        canvas.background_color("#ffffff")
        self.assertEqual(canvas.background_color(), "#FFFFFF")
        canvas.background_color("#Aa7Ebc")
        self.assertEqual(canvas.background_color(), "#AA7EBC")


    def test_set_canvas_color_must_be_str(self):
        canvas = Canvas(700, 500)
        with self.assertRaises(TypeError):
            canvas.background_color(999944)


    def test_set_canvas_color_must_be_formatted_correctly(self):
        canvas = Canvas(700, 500)
        with self.assertRaises(ValueError):
            canvas.background_color("FFFE40")
        with self.assertRaises(ValueError):
            canvas.background_color("#EEE56")
        with self.assertRaises(ValueError):
            canvas.background_color("FF0")
        with self.assertRaises(ValueError):
            canvas.background_color("FFG000")



'''class GraphicAdditionTests(TestCase):

    def setUp(self):
        self.canvas = Canvas(400, 400)


    def test_can_add_rectangle(self):
        self.canvas.add_rectangle(10, 10, 50, 100)
        self.assertIsInstance(
         self.canvas._graphics[-1],
         graphics.Rectangle
        )
        self.assertEqual(self.canvas._graphics[-1]._width, 50)
        self.assertEqual(self.canvas._graphics[-1]._height, 100)
        self.canvas.add_rectangle(10, 10, 50, 100, opacity=0.3, line_style="..")
        self.assertEqual(len(self.canvas._graphics), 2)
        self.assertEqual(self.canvas._graphics[-1]._opacity, 0.3)
        self.assertEqual(self.canvas._graphics[-1]._line_style, "..")
        self.assertEqual(self.canvas._graphics[-1]._line_width, 1)


    def test_can_add_line(self):
        self.canvas.add_line(10, 10, 50, 100)
        self.assertIsInstance(
         self.canvas._graphics[-1],
         graphics.Line
        )
        self.assertEqual(self.canvas._graphics[-1].x1, 10)
        self.assertEqual(self.canvas._graphics[-1].y2, 100)
        self.canvas.add_line(10, 10, 50, 100, line_color="#999999", line_style="..")
        self.assertEqual(len(self.canvas._graphics), 2)
        self.assertEqual(self.canvas._graphics[-1].line_color, "#999999")
        self.assertEqual(self.canvas._graphics[-1].line_style, "..")
        self.assertEqual(self.canvas._graphics[-1].line_width, 1)


    def test_can_add_polygon(self):
        self.canvas.add_polygon(10, 30, 100, 45, 45, 40)
        self.assertIsInstance(
         self.canvas._graphics[-1],
         graphics.Polygon
        )
        self.assertEqual(self.canvas._graphics[-1].coordinates[-1], 40)
        self.canvas.add_polygon(10, 30, 100, 45, 45, 40, opacity=0.1)
        self.assertEqual(len(self.canvas._graphics), 2)
        self.assertEqual(self.canvas._graphics[-1].opacity, 0.1)
        self.assertEqual(self.canvas._graphics[-1].line_width, 1)


    def test_can_add_text(self):
        self.canvas.add_text(10, 30, "TEXT")
        self.assertIsInstance(
         self.canvas._graphics[-1],
         graphics.Text
        )
        self.assertEqual(self.canvas._graphics[-1].text, "TEXT")
        self.canvas.add_text(10, 30, "TEXT", vertical_align="top")
        self.assertEqual(len(self.canvas._graphics), 2)
        self.assertEqual(self.canvas._graphics[-1]._vertical_align, "top")
        self.assertEqual(self.canvas._graphics[-1]._opacity, 1)
        self.assertEqual(self.canvas._graphics[-1]._line_width, 0)



class CanvasSvgTests(TestCase):

    def test_can_make_shell_svg(self):
        canvas = Canvas(300, 200)
        self.assertEqual(
         canvas.to_svg(),
         '<?xml version="1.0" encoding="UTF-8"?>\n'
         '<!-- Created with OmniCanvas (omnicanvas.readthedocs.io) -->\n'
         '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200">\n'
         '\n\n</svg>'
        )


    def test_canvas_svg_contains_graphic_svg(self):
        canvas = Canvas(300, 200)
        canvas.add_line(0, 0, 300, 200)
        self.assertEqual(
         canvas.to_svg(),
         "\n".join((
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<!-- Created with OmniCanvas (omnicanvas.readthedocs.io) -->\n'
          '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200">\n',
          canvas._graphics[0].to_svg(),
          "</svg>"
         ))
        )


    def test_canvas_background_svg(self):
        canvas = Canvas(300, 200, background_color="#123456")
        self.assertEqual(
         canvas.to_svg(),
         "\n".join((
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<!-- Created with OmniCanvas (omnicanvas.readthedocs.io) -->\n'
          '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200">',
          '<rect x="0" y="0" width="300" height="200" style="fill:#123456;stroke-width:0;" />\n',
          "</svg>"
         ))
        )



class CanvasSavingTests(TestCase):

    def tearDown(self):
        try:
            os.remove("test.svg")
        except OSError:
            pass


    def test_can_save_canvas_as_svg(self):
        canvas = Canvas(300, 200)
        canvas.save("test.svg")
        self.assertIn("test.svg", os.listdir())
        with open("test.svg") as f:
            self.assertEqual(f.read(), canvas.to_svg())'''
