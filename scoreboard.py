from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 270)
        self.level = 0
        self.next_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over.", align="center", font=FONT)

    def next_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level + 1}", align="left", font=("Courier", 18, "normal"))
        self.level += 1
