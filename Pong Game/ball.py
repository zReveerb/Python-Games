from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("slow")
        self.setposition(0,0)
        self.turtlesize(0.5,0.5)
        self.GOING = 60
        self.setheading(self.GOING)

    def refresh(self):
        self.setposition(0,0)

    def move(self):
        self.forward(3)

    def bounce(self):

        self.setheading(360-self.GOING)
        self.GOING += 60


