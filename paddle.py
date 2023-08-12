from turtle import Turtle

RIGHT_PADDLE_X_POS = 350
RIGHT_PADDLE_Y_POS = 0
LEFT_PADDLE_X_POS = -350
LEFT_PADDLE_Y_POS = 0


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.set_position(position.lower())

    def set_position(self, position):
        if position == "right":
            self.goto(RIGHT_PADDLE_X_POS, RIGHT_PADDLE_Y_POS)
        else:
            self.goto(LEFT_PADDLE_X_POS, LEFT_PADDLE_Y_POS)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
