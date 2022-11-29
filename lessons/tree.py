import turtle as t

def tree(x: float, y: float) -> None:
    """Tree."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    trunk_length: float = 80.0
    UP: float = 90.0
    branch(UP, trunk_length)
    t.update()

def branch(angle: float, length: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length < 5.0:
        ... # Do nothing. Base case!
    else:
        branch(angle + 25.0, length * 0.75)
        branch(angle - 25.0, length * 0.75)
    t.setheading(angle + 180.0)
    t.forward(length)

t.tracer(0, 0)
t.speed(0)
t.getscreen().onclick(tree)
t.done()