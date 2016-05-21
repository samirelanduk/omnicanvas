from unittest import main, TestCase
from omnicanvas.canvas import Canvas

class CanvasCreationTests(TestCase):

    def test_can_create_canvas(self):
        canvas = Canvas(700, 500)
        self.assertEqual(canvas.graphics, [])
        self.assertEqual(canvas.width, 700)
        self.assertEqual(canvas.height, 500)
        self.assertEqual(canvas.background_color, None)
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



if __name__ == "__main__":
    main()
