from turtle import Turtle
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.contador = 0
        self.high_score = 0
        self.game = Turtle()

    def write_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.setposition(-60,270)
        self.color("blue")
        self.write(f"Score: {self.contador}", False, "center", ("Comic Sans", 14, "normal"))
        if self.high_score == 0:
            self.high_score = self.contador
        elif self.high_score < self.contador:
            self.high_score = self.contador


    def add_points(self):
        self.contador += 1


    def reset(self):
        self.game.clear()
        self.game.penup()
        self.game.hideturtle()
        self.game.color("blue")

        if self.high_score >= self.contador:
            self.game.clear()
            self.game.setposition(60, 270)
            self.game.color("blue")
            self.game.write(f"High Score: {self.high_score}", False, "center", ("Comic Sans", 14, "normal"))
        self.contador = 0








