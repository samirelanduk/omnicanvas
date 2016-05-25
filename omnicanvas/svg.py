def generate_graphic_svg(graphic):
    return "stroke:%s;" % graphic.line_color


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
