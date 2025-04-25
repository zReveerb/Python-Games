from turtle import Turtle, Screen
from player import Player
from middle import Middle
from ball import Ball
import time
from scoreplayer1 import Score1
from score3 import Score2
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(750,500,0,0,)

player1 = Player()

player1.goto(x = -355, y = 0)
player2 = Player()
player2.goto(355,0)
screen.listen()

Thing = Ball()



MidScreen = Middle()
MidScreen.draw()
screen.update()
screen.onkey(player1.up,"w")
screen.onkey(player1.down, "s")
screen.title("PONG")


screen.onkey(player2.up, "Up")
screen.onkey(player2.down,"Down")

p1Score = Score1()
p2Score = Score2()
p1Score.write_score()
p2Score.write_score()
game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    Thing.move()
    if Thing.ycor() >= 240 or Thing.ycor() < -240:
        Thing.bounce()


    if Thing.xcor() >= player2.xcor()-20 and player2.ycor() + 25 >= Thing.ycor() >= player2.ycor() - 25:
        Thing.bounce()
    if Thing.xcor() <= player1.xcor()+20 and player1.ycor() + 25 >= Thing.ycor() >= player1.ycor() - 25:
        Thing.bounce()

    if Thing.xcor() > 360:
        p1Score.add_points()
        p1Score.write_score()
        Thing.refresh()
    elif Thing.xcor() < -360:
        p2Score.add_points()
        p2Score.write_score()
        Thing.refresh()

    if p1Score.contador == 7:
        p2Score.clear()
        p1Score.won()
        game_is_on = False
    if p2Score.contador == 7:
        p1Score.clear()
        p2Score.won()

screen.exitonclick()