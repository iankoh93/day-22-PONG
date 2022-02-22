from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(2)
        self.x_direction = 1
        self.y_direction = 1
        self.move_speed = 10

    def move(self):
        new_x = self.xcor() + self.move_speed * self.x_direction
        new_y = self.ycor() + self.move_speed * (600 / 800) * self.y_direction
        self.goto(x=new_x, y=new_y)

    def hit_wall(self):
        self.y_direction *= -1

    def hit_paddle(self):
        self.x_direction *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 10
        self.x_direction *= -1
