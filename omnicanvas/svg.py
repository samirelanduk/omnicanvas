import math

SVG_TEMPLATE = "\n".join([
    '<?xml version="1.0" encoding="utf-8"?>',
    '<!-- Generator: OmniCanvas  -->',
    '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">',
    '<svg width="%ipx" height="%ipx" xmlns="http://www.w3.org/2000/svg">',
    '<rect class="omnicanvas_background" x="0" y="0" width="100%%" height="100%%" fill="%s" />',
    '%s',
    '</svg>'
])

def get_line_dash(line):
    if line.line_style == "--":
        return "%i,%i" % (line.line_width * 10, line.line_width * 2)
    elif line.line_style == "..":
        return "%i,%i" % (line.line_width * 2, line.line_width * 2)
    else:
        return "none"


def canvas_to_svg(canvas):
    graphic_svgs = [graphic.to_svg() for graphic in canvas.graphics]
    return SVG_TEMPLATE % (
     canvas.width(),
     canvas.height(),
     canvas.background_color,
     "\t" + "\n\t".join(graphic_svgs))


def line_to_svg(line):
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%ipx" stroke-dasharray="%s" />' % (
     line.x1, line.y1, line.x2, line.y2, line.line_color, line.line_width, get_line_dash(line)
    )


def polyline_to_svg(polyline):
    return '<polyline points="%s" stroke="%s" stroke-width="%ipx" stroke-dasharray="%s" fill="none"/>' % (
     " ".join(["%.1f,%.1f" %  (x, y) for x, y in polyline.points]),
     polyline.line_color, polyline.line_width, get_line_dash(polyline)
    )


def rectangle_to_svg(rectangle):
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" stroke="%s" stroke-width="%ipx" stroke-dasharray="%s" fill="%s" fill-opacity="%.3f" />' % (
     rectangle.x, rectangle.y, rectangle.width, rectangle.height,
     rectangle.line_color, rectangle.line_width, get_line_dash(rectangle),
     rectangle.fill_color if rectangle.fill_color else "none", rectangle.opacity
    )
