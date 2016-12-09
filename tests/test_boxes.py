from unittest import TestCase
from omnicanvas.graphics import ShapeGraphic, BoxGraphic

class BoxGraphicCreationTests(TestCase):

    def test_can_create_box_graphic(self):
        box = BoxGraphic(10, 20, 100, 200)
        self.assertIsInstance(box, ShapeGraphic)
        self.assertEqual(box._x, 10)
        self.assertEqual(box._y, 20)
        self.assertEqual(box._width, 100)
        self.assertEqual(box._height, 200)
        self.assertEqual(box._fill_color, "#FFFFFF")
        self.assertEqual(box._opacity, 1)
        self.assertEqual(box._line_width, 1)
        self.assertEqual(box._line_style, "-")
        self.assertEqual(box._line_color, "#000000")
        self.assertEqual(box._rotation, (0, 0, 0))
        self.assertEqual(box._data, {})


    def test_box_location_must_be_numeric(self):
        with self.assertRaises(TypeError):
            BoxGraphic("10", 20, 100, 200)
        with self.assertRaises(TypeError):
            BoxGraphic(10, "20", 100, 200)
        BoxGraphic(10.5, 20, 100, 200)
        BoxGraphic(10, 20.5, 100, 200)


    def test_box_dimensions_must_be_numeric(self):
        with self.assertRaises(TypeError):
            BoxGraphic(10, 20, "100", 200)
        with self.assertRaises(TypeError):
            BoxGraphic(10, 20, 100, "200")
        BoxGraphic(10, 20, 100.5, 200)
        BoxGraphic(10, 20, 100, 200.5)



class BoxGraphicPropertyTests(TestCase):

    def test_basic_properties(self):
        box = BoxGraphic(10, 20, 100, 200)
        self.assertIs(box.x(), box._x)
        self.assertIs(box.y(), box._y)
        self.assertIs(box.width(), box._width)
        self.assertIs(box.height(), box._height)
