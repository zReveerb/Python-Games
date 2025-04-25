COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


from turtle import Turtle
import random
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(random.randint(310,800),random.randint(-240,280))
        self.shape("square")
        self.shapesize(1,2)
        self.setheading(180)
        self.contador = 1
        self.aleatorio = random.randint(-400, -310)

    def move(self):
        self.forward(self.contador)

    def faster(self):
        self.contador *= 1.1

    def refresh(self):
        if self.xcor() <= self.aleatorio:
            self.color(random.choice(COLORS))
            self.goto(random.randint(300,800), random.randint(-240, 280))
