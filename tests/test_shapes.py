from unittest import TestCase
from omnicanvas.graphics import Graphic, ShapeGraphic

class ShapeGraphicCreationTests(TestCase):

    def test_can_create_shape_graphic(self):
        shape = ShapeGraphic()
        self.assertIsInstance(shape, Graphic)
        self.assertEqual(shape.fill_color, "#FFFFFF")
        self.assertEqual(shape.opacity, 1)
        self.assertEqual(shape.line_width, 1)
        self.assertEqual(shape.line_style, "-")
        self.assertEqual(shape.line_color, "#000000")


    def test_can_create_shape_graphic_with_fill(self):
        shape = ShapeGraphic(fill_color="#FF0000")
        self.assertEqual(shape.fill_color, "#FF0000")


    def test_shape_creation_will_capitalise_color(self):
        shape = ShapeGraphic(fill_color="#ffff00")
        self.assertEqual(shape.fill_color, "#FFFF00")


    def test_shape_color_must_be_str(self):
        with self.assertRaises(TypeError):
            shape = ShapeGraphic(fill_color=333000)
        with self.assertRaises(TypeError):
            shape = ShapeGraphic(fill_color=None)


    def test_shape_color_must_be_formatted_correctly(self):
        with self.assertRaises(ValueError):
            shape = ShapeGraphic(fill_color="FFFF00")
        with self.assertRaises(ValueError):
            shape = ShapeGraphic(fill_color="#FFF00")
        with self.assertRaises(ValueError):
            shape = ShapeGraphic(fill_color="#FF0")
        with self.assertRaises(ValueError):
            shape = ShapeGraphic(fill_color="#FFFG00")


    def test_can_create_shape_graphic_with_opacity(self):
        shape = ShapeGraphic(opacity=0.5)
        self.assertEqual(shape.opacity, 0.5)


    def test_opacity_must_be_numeric(self):
        with self.assertRaises(TypeError):
            shape = ShapeGraphic(opacity="100")
        with self.assertRaises(TypeError):
            shape = ShapeGraphic(opacity=None)
        shape = ShapeGraphic(opacity=0.5)


    def test_opacity_must_be_between_0_and_1(self):
        with self.assertRaises(ValueError):
            shape = ShapeGraphic(opacity=-1)
        with self.assertRaises(ValueError):
            shape = ShapeGraphic(opacity=1.1)
        shape = ShapeGraphic(opacity=0)
        shape = ShapeGraphic(opacity=1)



class ShapeSvgTests(TestCase):

    def test_shape_can_produce_fill_svg(self):
        shape = ShapeGraphic()
        self.assertEqual(shape.shape_svg(), "fill:#FFFFFF;stroke:#000000;")
        shape = ShapeGraphic(fill_color="#67DE43")
        self.assertEqual(shape.shape_svg(), "fill:#67DE43;stroke:#000000;")


    def test_shape_can_produce_opacity_svg(self):
        shape = ShapeGraphic(opacity=0.34)
        self.assertEqual(
         shape.shape_svg(),
         "fill:#FFFFFF;fill-opacity:0.340;stroke:#000000;"
        )
