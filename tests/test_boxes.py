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
        self.assertEqual(box.fill_color, "#FFFFFF")
        self.assertEqual(box.opacity, 1)
        self.assertEqual(box.line_width, 1)
        self.assertEqual(box.line_style, "-")
        self.assertEqual(box.line_color, "#000000")
        self.assertEqual(box.rotation, (0, 0, 0))


    def test_box_location_must_be_numeric(self):
        with self.assertRaises(TypeError):
            box = BoxGraphic("10", 20, 100, 200)
        with self.assertRaises(TypeError):
            box = BoxGraphic(10, "20", 100, 200)
        box = BoxGraphic(10.5, 20, 100, 200)
        box = BoxGraphic(10, 20.5, 100, 200)


    def test_box_dimensions_must_be_numeric(self):
        with self.assertRaises(TypeError):
            box = BoxGraphic(10, 20, "100", 200)
        with self.assertRaises(TypeError):
            box = BoxGraphic(10, 20, 100, "200")
        box = BoxGraphic(10, 20, 100.5, 200)
        box = BoxGraphic(10, 20, 100, 200.5)
