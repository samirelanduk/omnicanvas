from unittest import TestCase
from omnicanvas.graphics import BoxGraphic, Rectangle

class RectangleCreationTests(TestCase):

    def test_can_create_rectangle(self):
        rectangle = Rectangle(10, 30, 400, 500)
        self.assertIsInstance(rectangle, BoxGraphic)
        self.assertEqual(rectangle.x, 10)
        self.assertEqual(rectangle.y, 30)
        self.assertEqual(rectangle.width, 400)
        self.assertEqual(rectangle.height, 500)
        self.assertEqual(rectangle.fill_color, "#FFFFFF")
        self.assertEqual(rectangle.opacity, 1)
        self.assertEqual(rectangle.line_width, 1)
        self.assertEqual(rectangle.line_style, "-")
        self.assertEqual(rectangle.line_color, "#000000")
        self.assertEqual(rectangle.rotation, (0, 0, 0))
        self.assertEqual(str(rectangle), "<Rectangle 400×500 at (10,30)>")



class SvgTests(TestCase):

    def test_can_make_basic_svg(self):
        rectangle = Rectangle(10, 30, 400, 500)
        self.assertEqual(
         rectangle.to_svg(),
         '<rect x="10.0" y="30.0" width="400.0" height="500.0"'
         ' style="fill:#FFFFFF;stroke:#000000;" />'
        )


    def test_can_create_rotated_rectangle_svg(self):
        rectangle = Rectangle(10, 30, 400, 500, rotation=(200, 200, 45))
        self.assertEqual(
         rectangle.to_svg(),
         '<rect x="10.0" y="30.0" width="400.0" height="500.0"'
         ' style="fill:#FFFFFF;stroke:#000000;" transform="rotate(45.0 200.0 200.0)" />'
        )
