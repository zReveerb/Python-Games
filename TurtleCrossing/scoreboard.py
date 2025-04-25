FONT = ("Courier", 18, "normal")

from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-235, 270)
        self.contador = 1
        self.color("black")
        self.hideturtle()

    def score(self):
        self.clear()
        self.write(f"Level: {self.contador}", False, "center", FONT)

    def addscore(self):
        self.contador += 1

    def over(self):
        self.setposition(0,0)
        self.write("GAME OVER", False, "center", ("Courier", 30, "normal"))