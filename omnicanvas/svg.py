def generate_shape_svg(shape):
    return "fill:%s;" % shape.fill_color


def generate_rectangle_svg(rectangle):
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" style="%s"/>' % (
     rectangle.x, rectangle.y, rectangle.width, rectangle.height, rectangle.shape_svg()
    )
