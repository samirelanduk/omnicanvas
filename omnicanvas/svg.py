def generate_rectangle_svg(rectangle):
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" />' % (
     rectangle.x, rectangle.y, rectangle.width, rectangle.height
    )
