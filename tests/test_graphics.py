from unittest import TestCase
from omnicanvas.graphics import Graphic

class GraphicCreationTests(TestCase):

    def test_can_create_graphic(self):
        graphic = Graphic()
