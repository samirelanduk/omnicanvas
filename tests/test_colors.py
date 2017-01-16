from unittest import TestCase
from omnicanvas.colors import hsl_to_rgb, pallete

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



class PaletteTests(TestCase):

    def test_can_produce_color(self):
        color = pallete()
        self.assertIsInstance(color, str)
        self.assertEqual(len(color), 7)
        self.assertEqual(color[0], "#")
        for char in color[1:]:
            self.assertIn(char, "0123456789ABCDEF")
