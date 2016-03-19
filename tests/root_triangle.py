import unittest
import sys
sys.path.append(".")
import omnicanvas
import math

canvas = omnicanvas.Canvas(500, 500)
for n in range(10):
    canvas.draw_line(
     0, 500 * (n/10),
     500, 500 * (n/10),
     line_color="#AAAAAA",
     line_opacity=0.8
    )
    canvas.draw_line(
     500 * (n/10), 0,
     500 * (n/10), 500,
     line_color="#AAAAAA",
     line_opacity=0.8
    )
    canvas.draw_rectangle(
     0, 0, 500, 500
    )

one = 75
center = (canvas.width() / 2, canvas.height() / 2)
base_vertex = (center[0] + one, center[1])

tri_num = 16
for n in range(1, tri_num +1):
    print("Triangle %i:" % n)
    print("\tBase vertex: (%.3f, %.3f)" % base_vertex)
    base_gradient = (center[1] - base_vertex[1]) / (base_vertex[0] - center[0])\
     if base_vertex[0] - center[0] != 0 else float("inf")
    print("\tBase gradient: %.3f" % base_gradient)

    one_gradient = -1 / base_gradient if base_gradient != 0 else float("inf")
    print("\tOne gradient: %.3f" % one_gradient)

    base_vertex_angle = 90 - abs(math.degrees(math.atan(one_gradient)))
    print("\tBase vertex angle: %.3f" % base_vertex_angle)

    delta_x = abs(math.sin(math.radians(base_vertex_angle)) * one)
    delta_y = abs(math.cos(math.radians(base_vertex_angle)) * one)
    if base_vertex[1] < center[1]:
        delta_x *= -1
    if base_vertex[0] > center[0]:
        delta_y *= -1
    print("\tdx: %.3f" % delta_x)
    print("\tdy: %.3f" % delta_y)

    third_point = (base_vertex[0] + delta_x, base_vertex[1] + delta_y)
    print("\tThird point: (%.3f, %.3f)" % third_point)

    canvas.draw_polygon(
     *center, *base_vertex, *third_point,
     fill_color="#%02xFF%02x" % (
      int(255 * ((tri_num-n)/tri_num)), int(255 * (n/tri_num))
     ),
     opacity=0.7,
     line_style="..",
     line_width=1,
     line_opacity=0.5
    )
    base_vertex = third_point

canvas.save("svg", "svgs/root_triangle.svg")
