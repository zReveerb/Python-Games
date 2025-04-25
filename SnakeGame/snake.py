from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.lista = []
        self.create_snake()
    def create_snake(self):
        x = -40
        for i in range(0,3):
            tim = Turtle()
            tim.color("white")
            tim.penup()
            tim.shape("square")
            tim.setposition(x,0)
            x +=20
            self.lista.append(tim)
    def get_bigger(self):
        tim = Turtle()
        tim.color("white")
        tim.penup()
        tim.shape("square")
        xc = self.lista[len(self.lista)-1].xcor()
        yc = self.lista[len(self.lista)-1].ycor()
        tim.setposition(xc,yc)
        self.lista.append(tim)
    def reset(self):
        for k in self.lista:
            k.hideturtle()
        self.lista.clear()
        x = -40
        for j in range(0, 3):
            tim = Turtle()
            tim.color("white")
            tim.penup()
            tim.shape("square")
            tim.setposition(x, 0)
            x += 20
            self.lista.append(tim)
    def move(self):
        for seg_num in range(len(self.lista) - 1, 0, -1):
            new_x = self.lista[seg_num - 1].xcor()
            new_y = self.lista[seg_num - 1].ycor()
            self.lista[seg_num].goto(new_x, new_y)
        self.lista[0].forward(20)

    def up(self):
        if self.lista[0].heading() != DOWN:
            self.lista[0].setheading(UP)
    def down(self):
        if self.lista[0].heading() != UP:
            self.lista[0].setheading(DOWN)
    def left(self):
        if self.lista[0].heading() != RIGHT:
            self.lista[0].setheading(LEFT)
    def right(self):
        if self.lista[0].heading() != LEFT:
            self.lista[0].setheading(RIGHT)
