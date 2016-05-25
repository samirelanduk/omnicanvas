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


def generate_shape_svg(shape):
    opacity = "fill-opacity:%.3f;" % shape.opacity
    return "fill:%s;%s%s" % (
     shape.fill_color,
     opacity if shape.opacity != 1 else "",
     shape.graphic_svg()
    )


def generate_rectangle_svg(rectangle):
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" style="%s" />' % (
     rectangle.x, rectangle.y, rectangle.width, rectangle.height, rectangle.shape_svg()
    )


def generate_line_svg(line):
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" style="%s" />' % (
     line.x1, line.y1, line.x2, line.y2, line.graphic_svg()
    )


def generate_polygon_svg(polygon):
    return '<polygon points="%s" style="%s" />' % (
     ", ".join(["%.1f,%.1f" % (
      point[0], point[1]
     ) for point in polygon.coordinates_to_xy_pairs()]),
     polygon.shape_svg()
    )


def generate_text_svg(text):
    if text.horizontal_align not in ("left", "center", "right"):
        raise ValueError(
         "'%s' is not a valid horizontal_align value" % text.horizontal_align
        )
    horizontal_align = {
     "left": "start",
     "center": "middle",
     "right": "end"
    }[text.horizontal_align]
    return '<text x="%.1f" y="%.1f" text-anchor="%s" style="%s">%s</text>' % (
     text.x,
     text.y,
     horizontal_align,
     text.graphic_svg(),
     text.text
    )
