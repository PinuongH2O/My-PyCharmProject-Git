import turtle
import time

# tạo màn hình
screen = turtle.Screen()
screen.title("Mini Geometry Dash")
screen.bgcolor("black")
screen.setup(width=600, height=400)
screen.tracer(0)

# tạo player
player = turtle.Turtle()
player.shape("square")
player.color("Green")
player.penup()
player.goto(-200, -100)

# tạo obstacle
obs = turtle.Turtle()
obs.shape("square")
obs.color("Yellow")
obs.penup()
obs.goto(300, -100)

gravity = -0.5
velocity = 0
jumping = False
def jump():
    global velocity, jumping
    if not jumping:
        velocity = 10
        jumping = True

screen.listen()
screen.onkey(jump, "space")
while True:
    screen.update()

    # gravity
    velocity += gravity
    y = player.ycor()
    y += velocity

    if y < -100:
        y = -100
        jumping = False

    player.sety(y)

    # obstacle chạy
    x = obs.xcor()
    x -= 5
    if x < -300:
        x = 300
    obs.setx(x)

    # va chạm
    if player.distance(obs) < 20:
        print("Game Over!")
        break

    time.sleep(0.02)