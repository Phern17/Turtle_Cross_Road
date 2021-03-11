from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
MAX_TOP = 250
MAX_BOT = -250


class CarManager:

    def __init__(self):
        super().__init__()
        self.car_batch = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_num = random.randint(1, 6)
        if random_num == 6:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            starting_ypos = random.randint(MAX_BOT, MAX_TOP)
            car.goto(300, starting_ypos)
            self.car_batch.append(car)

    def car_move(self, level, move):
        if move:
            for car in self.car_batch:
                car.backward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT