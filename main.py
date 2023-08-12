from turtle import Screen
from Paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()