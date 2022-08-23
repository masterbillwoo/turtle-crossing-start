COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Screen, Turtle, forward
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)

    def move_forward(self):
        self.forward(STARTING_MOVE_DISTANCE)