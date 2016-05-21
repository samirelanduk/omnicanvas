from unittest import TestCase
from omnicanvas.graphics import ShapeGraphic, BoxGraphic

class BoxGraphicCreationTests(TestCase):

    def test_can_create_box_graphic(self):
        box = BoxGraphic(10, 20, 100, 200)
        self.assertIsInstance(box, ShapeGraphic)
        self.assertEqual(box.x, 10)
        self.assertEqual(box.y, 20)
        self.assertEqual(box.width, 100)
        self.assertEqual(box.height, 200)
