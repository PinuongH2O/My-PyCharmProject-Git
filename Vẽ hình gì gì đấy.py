import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

colors = ["Pink","Orange","Blue","Yellow","Red","Green","Purple",]

for i in range(100):
    t.pencolor(colors[i % 7])
    t.forward(i * 3)
    t.right(90)
screen.listen()
screen.onkey(lambda: t.hideturtle(), key="h")


turtle.done()