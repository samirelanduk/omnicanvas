from unittest import TestCase
from omnicanvas.graphics import BoxGraphic, Rectangle

class RectangleCreationTests(TestCase):

    def test_can_create_rectangle(self):
        rectangle = Rectangle(10, 30, 400, 400)
        self.assertIsInstance(rectangle, BoxGraphic)
        self.assertEqual(rectangle.x, 10)
        self.assertEqual(rectangle.y, 30)
        self.assertEqual(rectangle.width, 400)
        self.assertEqual(rectangle.height, 400)
        self.assertEqual(rectangle.fill_color, "#FFFFFF")
        self.assertEqual(rectangle.opacity, 1)
        self.assertEqual(rectangle.line_width, 1)
        self.assertEqual(rectangle.line_style, "-")
        self.assertEqual(rectangle.line_color, "#000000")
