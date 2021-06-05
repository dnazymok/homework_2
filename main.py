import turtle


def hilbert_curve(order):
    # replacement rules
    a = "−BF+AFA+FB−"
    b = "+AF−BFB−FA+"
    # start
    path = "A"

    for i in range(order):
        path = path.replace("A", a.lower())
        path = path.replace("B", b.lower())
        path = path.upper()

    turtle.tracer(1, 0)

    for i in path:
        if i == "F":
            turtle.forward(5)
        elif i == "−":
            turtle.left(90)
        elif i == "+":
            turtle.right(90)
    turtle.done()


hilbert_curve(5)
