from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars : list[Turtle] = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            nc = Turtle("square")
            nc.shapesize(stretch_wid=1, stretch_len=2)
            nc.penup()
            nc.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            nc.goto(300, random_y)
            self.cars.append(nc)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
