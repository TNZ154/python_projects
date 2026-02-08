import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
t = turtle.Turtle()
t.speed(3)
t.pencolor("darkgreen")
t.pensize(3)
for i in range(3):
    t.forward(100)
    t.left(120)

turtle.done()