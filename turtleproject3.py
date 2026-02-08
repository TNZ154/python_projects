import turtle

t = turtle.Turtle()
t.pencolor("blue")
t.pensize(5)
wm = turtle.Screen()
wm.bgcolor("black")
for i in range(6):
	t.forward(90)
	t.left(300)

turtle.done()