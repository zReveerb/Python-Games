from turtle import Turtle

class Middle(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.setposition(0, -250)
        self.setheading(90)
        self.pendown()
        self.pensize(5)


    def draw(self):
        while self.ycor() < 250:
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()