from unittest import TestCase
from omnicanvas.graphics import BoxGraphic, Rectangle

class RectangleCreationTests(TestCase):

    def test_can_create_rectangle(self):
        rectangle = Rectangle()
        self.assertIsInstance(rectangle, BoxGraphic)
