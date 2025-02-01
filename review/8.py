import turtle

t = turtle.Turtle()

# for i in range(10):
#     t.circle(30)
#     t.right(36)
# t.speed("fastest")
# t.color("red")
# for i in range(6):
#     t.circle(60,60)
#     t.left(120)
#     t.circle(60,60)
#     t.left(120)
#     t.right(60)

t.fillcolor("blue")
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()

t.fillcolor("darkblue")
t.penup()
t.goto(10, -10)
t.pendown()
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
t.end_fill()
turtle.done()