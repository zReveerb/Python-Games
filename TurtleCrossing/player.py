STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.setposition(0,-280)
        self.shape("turtle")
        self.setheading(90)

    def refresh(self):
        self.setposition(STARTING_POSITION)

    def move(self):
        self.setposition(0, self.ycor()+5)