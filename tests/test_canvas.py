from unittest import main, TestCase
from omnicanvas.canvas import Canvas

class CanvasCreationTests(TestCase):

    def test_can_create_canvas(self):
        canvas = Canvas(700, 500)
        self.assertEqual(canvas.graphics, [])
        self.assertEqual(canvas.width, 700)
        self.assertEqual(canvas.height, 500)
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



if __name__ == "__main__":
    main()
