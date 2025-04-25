from turtle import Turtle
import random

class Score2(Turtle):
    def __init__(self):
        super().__init__()
        self.contador = 0

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.setposition(200,200)
        self.color("blue")
        self.write(f"{self.contador}", False, "center", ("Arial",30, "normal"))

    def add_points(self):
        self.contador += 1

    def won(self):
        self.clear()
        self.setposition(0,0)
        self.write("Player 2 Won! Game OVER", False, "center", ("Arial", 20, "normal"))