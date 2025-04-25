import pandas
from turtle import Turtle
class Name:
    def __init__(self):
        self.tim = Turtle()
        self.data = pandas.read_csv("50_states.csv")

    def write(self, state):
        self.tim.penup()
        self.tim.hideturtle()
        self.tim.color("black")
        row = self.data[self.data["state"] == state]
        x = row.x
        x = x.to_list()
        row2= self.data[self.data["state"] == state]
        y = row2.y
        y = y.to_list()
        self.tim.goto(x[0],y[0])
        self.tim.write(f"{state}", False, "center", ("Comic Sans", 10, "normal"))



