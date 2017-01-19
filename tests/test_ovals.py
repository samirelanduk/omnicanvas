from unittest import TestCase
from omnicanvas.graphics import BoxGraphic, Oval

class OvalCreationTests(TestCase):

    def test_can_create_oval(self):
        oval = Oval(10, 30, 400, 500)
        self.assertIsInstance(oval, BoxGraphic)
        self.assertEqual(oval._x, 10)
        self.assertEqual(oval._y, 30)
        self.assertEqual(oval._width, 400)
        self.assertEqual(oval._height, 500)
        self.assertEqual(oval._fill_color, "#FFFFFF")
        self.assertEqual(oval._opacity, 1)
        self.assertEqual(oval._line_width, 1)
        self.assertEqual(oval._line_style, "-")
        self.assertEqual(oval._line_color, "#000000")
        self.assertEqual(oval._rotation, (0, 0, 0))
        self.assertEqual(oval._data, {})


    def test_oval_repr(self):
        oval = Oval(10, 30, 400, 500)
        self.assertEqual(str(oval), "<Oval 400×500 at (10,30)>")
