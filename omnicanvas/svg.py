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
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" style="%s"/>' % (
     rectangle.x, rectangle.y, rectangle.width, rectangle.height, rectangle.shape_svg()
    )
