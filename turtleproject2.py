import turtle
 
t = turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("lightblue")

def draw_rectangle(length, width):
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(length)
        else:
            turtle.forward(width)
        turtle.right(90)

draw_rectangle(200, 100)
turtle.done()