from unittest import TestCase
import omnicanvas
import omnicanvas.color
from omnicanvas.color import hsl_to_rgb, colors

class HslConversionTests(TestCase):

    def test_can_convert_colors(self):
        self.assertEqual(
         hsl_to_rgb(108, 100, 50),
         "#32FF00"
        )
        self.assertEqual(
         hsl_to_rgb(8, 87, 31),
         "#931C0A"
        )
        self.assertEqual(
         hsl_to_rgb(300, 6, 61),
         "#A195A1"
        )


    def test_arguments_must_be_numeric(self):
        with self.assertRaises(TypeError):
            hsl_to_rgb("108", 100, 50)
        with self.assertRaises(TypeError):
            hsl_to_rgb(108, "100", 50)
        with self.assertRaises(TypeError):
            hsl_to_rgb(108, 100, "50")
        hsl_to_rgb(108.5, 99.5, 50.5)


    def test_hue_must_be_in_degrees(self):
        with self.assertRaises(ValueError):
            hsl_to_rgb(-1, 100, 50)
        with self.assertRaises(ValueError):
            hsl_to_rgb(361, 100, 50)


    def test_saturation_must_be_percent(self):
        with self.assertRaises(ValueError):
            hsl_to_rgb(0, -1, 50)
        with self.assertRaises(ValueError):
            hsl_to_rgb(360, 101, 50)


    def test_lightness_must_be_percent(self):
        with self.assertRaises(ValueError):
            hsl_to_rgb(0, 50, -1)
        with self.assertRaises(ValueError):
            hsl_to_rgb(360, 50, 101)


    def test_hsl_converter_imported_to_root(self):
        self.assertIs(omnicanvas.hsl_to_rgb, hsl_to_rgb)



class ColorConstantTests(TestCase):

    def test_all_named_colors_in_list(self):
        color_constants = [var for var in dir(omnicanvas.color) if var.isupper()]
        for color in color_constants:
            self.assertIn(getattr(omnicanvas.color, color), colors)


    def test_all_named_colors_imported_to_root(self):
        color_constants = [var for var in dir(omnicanvas.color) if var.isupper()]
        for color in color_constants:
            getattr(omnicanvas, color)


    def test_colors_imported_to_root(self):
        self.assertIs(omnicanvas.colors, colors)
