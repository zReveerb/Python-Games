from turtle import Turtle, Screen
screen = Screen()
tim = Turtle()
screen.setup(width=600,height=600)
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setposition(-30,280)
tim.color("blue")
tim.write("Score:", False, "center", ("Comic Sans", 12, "normal" ))

peido = 10

james = Turtle()
james.penup()
james.hideturtle()
james.speed("fastest")
james.setposition(20,280)
james.color("blue")
james.write(peido, False, "center", ("Comic Sans", 12, "normal" ))



screen.exitonclick()