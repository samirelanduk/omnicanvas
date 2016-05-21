from unittest import TestCase
from omnicanvas.graphics import Graphic, ShapeGraphic

class ShapeGraphicCreationTests(TestCase):

    def test_can_create_shape_graphic(self):
        shape = ShapeGraphic()
        self.assertIsInstance(shape, Graphic)
