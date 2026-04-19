import turtle

screen = turtle.Screen()
screen.title("Paint")


player = turtle.Turtle()
player.shape("classic")
player.color("green")


def move_up():
    player.setheading(90)  # quay rùa lên trên
    player.sety(player.ycor() + 10)

def move_down():
    player.setheading(270)  # quay rùa xuống dưới
    player.sety(player.ycor() - 10)

def move_left():
    player.setheading(180)  # quay rùa sang trái
    player.setx(player.xcor() - 10)

def move_right():
    player.setheading(0)  # quay rùa sang phải
    player.setx(player.xcor() + 10)

def pen_up():
    player.penup()

def pen_down():
    player.pendown()

def pen_hide():
    player.hideturtle()

def pen_show():
    player.showturtle()

def clear_screen():
    player.clear()


screen.listen()
screen.onkey(move_up, "w") # nhấn W để lên trên
screen.onkey(move_down, "s") # nhấn S để xuống dưới
screen.onkey(move_left, "a") # nhấn A để sang trái
screen.onkey(move_right, "d") # nhấn D để sang phải
screen.onkey(pen_up, "q")     # nhấn Q để nhấc bút
screen.onkey(pen_down, "e")   # nhấn E để hạ bút
screen.onkey(pen_hide, "h")  # nhấn H để ẩn rùa
screen.onkey(pen_show, "j")  # nhấn J để hiện rùa
screen.onkey(clear_screen, "c") # nhấn C để xoá màn hình
screen.onkey(lambda: player.pencolor("red"), "1") # nhấn 1 để đổi thành màu đỏ
screen.onkey(lambda: player.pencolor("green"), "2") # nhấn 2 để đổi thành màu đỏ
screen.onkey(lambda: player.pencolor("blue"), "3")  # nhấn 3 để đổi thành màu đỏ
screen.onkey(lambda: player.pencolor("yellow"), "4")
screen.onkey(lambda: player.pencolor("purple"), "5")
screen.onkey(lambda: player.pencolor("orange"), "6")
screen.onkey(lambda: player.pencolor("black"), "7")
screen.onkey(lambda: player.pencolor("white"), "0")

turtle.done()