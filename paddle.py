from turtle import Turtle

STARTING_X_POS = 350
STARTING_Y_POS = 0
MOVE_DISTANCE = 30
UP = 90
LENGTH_OF_PADDLE = 5


class Paddle(Turtle):

    def __init__(self, x_cor=STARTING_X_POS):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=LENGTH_OF_PADDLE)
        self.speed("fastest")
        self.setheading(UP)
        self.goto(x=x_cor, y=STARTING_Y_POS)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.forward(-MOVE_DISTANCE)
