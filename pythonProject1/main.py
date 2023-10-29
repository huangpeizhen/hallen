import turtle as t  # 画圆


def the2nd_circle():
    t.begin_fill()
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.circle(100)
    t.fillcolor("purple")
    t.end_fill()


def math(x):
    if x <= 0:
        return 0
    return math(x - 1) + x


if __name__ == '__main__':
    for i in range(100):
        if i == 50:
            continue

        sum = math(i)
        print(sum)


    t.begin_fill()
    t.pensize(1)
    t.speed(20)
    t.setheading(0)
    t.pencolor("red")
    t.fillcolor("yellow")
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.circle(150)
    t.end_fill()

    # Hide the turtle cursor
    t.hideturtle()
    # 第二个圆
    for i in range(10):
        the2nd_circle()

    # 第三个圆
    t.begin_fill()
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.circle(50)
    t.fillcolor("blue")
    t.end_fill()
    # 在第三个圆里画一个三角形
    t.begin_fill()
    t.penup()
    t.goto(0, +50)
    t.pendown()
    t.right(120)
    t.forward(86)
    t.left(120)
    t.forward(86)
    t.left(120)
    t.forward(86)
    t.fillcolor("pink")
    t.end_fill()
    # Keep the window open
    t.done()
