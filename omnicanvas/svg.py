SVG_TEMPLATE = "\n".join([
    '<?xml version="1.0" encoding="utf-8"?>',
    '<!-- Generator: OmniCanvas  -->',
    '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">',
    '<svg width="%ipx" height="%ipx" xmlns="http://www.w3.org/2000/svg">',
    '%s',
    '</svg>'
])


def canvas_to_svg(canvas):
    return SVG_TEMPLATE % (canvas.width(), canvas.height(), "")
