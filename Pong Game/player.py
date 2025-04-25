from turtle import Turtle
import random

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.turtlesize(3,1,0)
        self.color("white")
        self.speed("fastest")

    def up(self):
        if self.ycor() < 220:
            y = self.ycor() + 10
            self.goto(self.xcor(), y)
    def down(self):
        if self.ycor() > -220:
            y = self.ycor() - 10
            self.goto(self.xcor(), y)