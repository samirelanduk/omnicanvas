import unittest
import sys
sys.path.append(".")
from omnicanvas.graphics import *


box = GenericBox(10, 10, 100, 100)
outline = GenericLine("-", 1, "#000000")
shape = GenericShape("FF0000", 0.5)

line = Line()
path = Path()
rectangle = Rectangle()
polygon = Polygon()
oval = Oval()
arc = Arc()
text = Text()
