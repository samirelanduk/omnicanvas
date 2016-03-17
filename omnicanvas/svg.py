import math

SVG_TEMPLATE = "\n".join([
    '<?xml version="1.0" encoding="utf-8"?>',
    '<!-- Generator: OmniCanvas  -->',
    '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" '
    '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">',
    '<svg width="%ipx" height="%ipx" xmlns="http://www.w3.org/2000/svg">',
    '<rect class="omnicanvas_background" x="0" y="0" '
    'width="100%%" height="100%%" fill="%s" />',
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
    return '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1fpx" stroke-dasharray="%s" />' % (
     line.x1, line.y1, line.x2, line.y2, line.line_color, line.line_width, get_line_dash(line)
    )


def polyline_to_svg(polyline):
    return '<polyline points="%s" stroke="%s" stroke-width="%.1fpx" stroke-dasharray="%s" fill="none" />' % (
     " ".join(["%.1f,%.1f" %  (x, y) for x, y in polyline.points]),
     polyline.line_color, polyline.line_width, get_line_dash(polyline)
    )


def rectangle_to_svg(rectangle):
    return '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" stroke="%s" stroke-width="%.1fpx" stroke-dasharray="%s" fill="%s" fill-opacity="%.3f" />' % (
     rectangle.x, rectangle.y, rectangle.width, rectangle.height,
     rectangle.line_color, rectangle.line_width, get_line_dash(rectangle),
     rectangle.fill_color if rectangle.fill_color else "none", rectangle.opacity
    )


def polygon_to_svg(polygon):
    return '<polygon points="%s" stroke="%s" stroke-width="%.1fpx" stroke-dasharray="%s" fill="%s" fill-opacity="%.3f" />' % (
     " ".join(["%.1f,%.1f" %  (x, y) for x, y in polygon.points]),
     polygon.line_color, polygon.line_width, get_line_dash(polygon),
     polygon.fill_color if polygon.fill_color else "none", polygon.opacity
    )


def oval_to_svg(oval):
    return '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" stroke="%s" stroke-width="%.1fpx" stroke-dasharray="%s" fill="%s" fill-opacity="%.3f" />' % (
     oval.center()[0], oval.center()[1], oval.width  /2, oval.height / 2,
     oval.line_color, oval.line_width, get_line_dash(oval),
     oval.fill_color if oval.fill_color else "none", oval.opacity
    )


def arc_to_svg(arc):
    start_point = get_point_from_angle(
     arc.center()[0], arc.center()[1], arc.width, arc.height, arc.start_angle
    )
    end_point = get_point_from_angle(
     arc.center()[0], arc.center()[1], arc.width, arc.height, arc.end_angle
    )
    greater_than_180 = (
     arc.end_angle > arc.start_angle and arc.end_angle - arc.start_angle > 180
    ) or (
     arc.end_angle < arc.start_angle and arc.end_angle + (360 - arc.start_angle) > 180
    )
    return '<path d="M %.1f,%.1f A %.1f,%.1f 0 %i 0 %.1f,%.1f%s" stroke="%s" stroke-width="%.1fpx" stroke-dasharray="%s" fill="%s" fill-opacity="%.3f" />' % (
     start_point[0], start_point[1],
     arc.width / 2, arc.height / 2,
     1 if greater_than_180 else 0,
     end_point[0], end_point[1],
     " L%.1f,%.1f L%.1f,%.1f" % (
      arc.center()[0], arc.center()[1], start_point[0], start_point[1]
     ) if arc.connect else "",
     arc.line_color, arc.line_width, get_line_dash(arc),
     arc.fill_color if arc.fill_color else "none", arc.opacity
    )


def text_to_svg(text):
    anchor = None
    alignment = None
    if text.horizontal_align == "center":
        anchor = "middle"
    elif text.horizontal_align == "left":
        anchor = "start"
    elif text.horizontal_align == "right":
        anchor = "end"
    if text.vertical_align == "center":
        alignment = "middle"
    elif text.vertical_align == "top":
        alignment = "hanging"
    elif text.vertical_align == "bottom":
        alignment = "baseline"
    return '<text x="%.1f" y="%.1f" fill="%s" font-family="%s" style="font-size:%ipx" text-anchor="%s" alignment-baseline="%s">%s</text>' % (
     text.x, text.y, text.color, text.font_family, text.font_size, anchor, alignment, text.text
    )


def get_point_from_angle(cx, cy, width, height, angle):
    a = width / 2
    b = height / 2
    if angle == 90:
        return (cx, cy - b)
    elif angle == 270:
        return (cx, cy + b)
    else:
        denominator = math.sqrt(
         (b ** 2) + ((a ** 2) * (math.tan(math.radians(angle)) ** 2))
        )
        ab = a * b
        ab_tan_angle = ab * math.tan(math.radians(angle))
        if (0 <= angle < 90) or (270 < angle <= 360):
            return (cx + (ab / denominator), cy - (ab_tan_angle / denominator))
        else:
            return (cx - (ab / denominator), cy + (ab_tan_angle / denominator))
