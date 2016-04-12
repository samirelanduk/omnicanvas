import omnicanvas
canvas = omnicanvas.Canvas(500, 300, background_color="#A8CCF0")
canvas.draw_rectangle(10, 10, 200, 200, fill_color="#D92626", line_width=0)
canvas.draw_rectangle(290, 90, 200, 200, fill_color="#144BB8", line_width=0)
canvas.draw_oval(150, 50, 200, 200, fill_color="#00FF00", opacity=0.4)

canvas.save("svg", "docs/source/example.svg")
