from unittest import TestCase
from omnicanvas.graphics import ShapeGraphic, BoxGraphic

class BoxGraphicCreationTests(TestCase):

    def test_can_create_box_graphic(self):
        box = BoxGraphic()
        self.assertIsInstance(box, ShapeGraphic)
