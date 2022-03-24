import turtle
import random


class Food (turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))