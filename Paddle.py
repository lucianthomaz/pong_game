from turtle import Turtle

RIGHT_PADDLE_X_POS = 350
RIGHT_PADDLE_Y_POS = 0


class Paddle:

    def __init__(self):
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.set_position(RIGHT_PADDLE_X_POS, RIGHT_PADDLE_Y_POS)

    def set_position(self, x_pos, y_pos):
        self.paddle.goto(x_pos, y_pos)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
