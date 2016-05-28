def generate_graphic_svg(graphic):
    width = "stroke-width:%.1f;" % graphic.line_width
    if graphic.line_style not in ("-", "--", ".."):
        raise ValueError("'%s' is not a valid line style" % str(graphic.line_style))
    pattern = "stroke-dasharray:%s;" % {
     "-": "1,0",
     "--": "%.1f,%.1f" % (10 * graphic.line_width, 5 * graphic.line_width),
     "..": "%.1f,%.1f" % (1 * graphic.line_width, 2 * graphic.line_width)
    }[graphic.line_style]

    return "stroke:%s;%s%s" % (
     graphic.line_color,
     width if graphic.line_width != 1 else "",
     pattern if graphic.line_style != "-" else ""
    )


def generate_rotation_svg(graphic):
    if graphic.rotation != (0, 0, 0):
        if not isinstance(graphic.rotation, tuple):
            raise TypeError(
             "Rotations must be tuples, not '%s'" % str(graphic.rotation)
            )
        if len(graphic.rotation) != 3:
            raise ValueError(
             "Rotations must be tuples of length 3, not %i" % len(graphic.rotation)
            )
        for value in graphic.rotation:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("Rotation values must be numeric, not '%s'" % value)
        if not 0 <= graphic.rotation[2] <= 360:
            raise ValueError(
             "Rotation must be between 0 and 360, not %s" % str(graphic.rotation[2])
            )
    return (' transform="rotate(%.1f %.1f %.1f)"' % (
     graphic.rotation[2], graphic.rotation[0], graphic.rotation[1]
    )) if graphic.rotation != (0, 0, 0) else ""


def generate_data_svg(graphic):
    if not isinstance(graphic.data, dict):
        raise TypeError("Data must be dict, not '%s'" % graphic.data)
    return " " + " ".join(
     ['%s="%s"' % (str(key), str(graphic.data[key])) for key in graphic.data]
    ) if graphic.data else ""


def generate_shape_svg(shape):
    opacity = "fill-opacity:%.3f;" % shape.opacity
    return "fill:%s;%s%s" % (
     shape.fill_color,
     opacity if shape.opacity != 1 else "",
     shape.graphic_svg()
    )


def generate_rectangle_svg(rectangle):
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" style="%s"%s%s />' % (
     rectangle.x,
     rectangle.y,
     rectangle.width,
     rectangle.height,
     rectangle.shape_svg(),
     rectangle.rotation_svg(),
     rectangle.data_svg()
    )


def generate_line_svg(line):
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" style="%s"%s%s />' % (
     line.x1,
     line.y1,
     line.x2,
     line.y2,
     line.graphic_svg(),
     line.rotation_svg(),
     line.data_svg()
    )


def generate_polygon_svg(polygon):
    return '<polygon points="%s" style="%s"%s%s />' % (
     ", ".join(["%.1f,%.1f" % (
      point[0], point[1]
     ) for point in polygon.coordinates_to_xy_pairs()]),
     polygon.shape_svg(),
     polygon.rotation_svg(),
     polygon.data_svg(),
    )


def generate_text_svg(text):
    if text.horizontal_align not in ("left", "center", "right"):
        raise ValueError(
         "'%s' is not a valid horizontal_align value" % text.horizontal_align
        )
    horizontal_align = {
     "left": "end",
     "center": "middle",
     "right": "start"
    }[text.horizontal_align]
    if text.vertical_align not in ("top", "center", "bottom"):
        raise ValueError(
         "'%s' is not a valid vertical_align value" % text.vertical_align
        )
    vertical_align = {
     "top": "baseline",
     "center": "middle",
     "bottom": "hanging"
    }[text.vertical_align]
    return '<text x="%.1f" y="%.1f" text-anchor="%s" alignment-baseline="%s" style="font-size:%.1f;%s"%s%s>%s</text>' % (
     text.x,
     text.y,
     horizontal_align,
     vertical_align,
     text.font_size,
     text.shape_svg(),
     text.rotation_svg(),
     text.data_svg(),
     text.text
    )


SVG_BASE = """<?xml version="1.0" encoding="UTF-8"?>
<!-- Created with OmniCanvas (omnicanvas.readthedocs.io) -->
<svg xmlns="http://www.w3.org/2000/svg" width="%i" height="%i">
%s
%s
</svg>"""


def generate_canvas_svg(canvas):
    return SVG_BASE % (
     canvas.width,
     canvas.height,
     ('<rect x="0" y="0" width="%i" height="%i" style="fill:%s;stroke-width:0;" />' % (
      canvas.width, canvas.height, canvas.background_color
     )) if canvas.background_color else "",
     "\n".join(
      [graphic.to_svg() for graphic in canvas.graphics]
     )
    )
