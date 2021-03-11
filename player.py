STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color('black')
        self.penup()
        self.starting_point()
        self.setheading(90)

    def turtle_move(self):
        new_cory = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_cory)

    def starting_point(self):
        self.goto(STARTING_POSITION)