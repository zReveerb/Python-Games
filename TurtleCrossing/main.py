import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
lista = []

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
player1 = Player()
screen.listen()

score = Scoreboard()
score.score()
screen.onkey(player1.move, "w")

game = True
for i in range(0, 16):
    car = CarManager()
    lista.append(car)



while game:
    time.sleep(0.01)
    screen.update()
    if player1.ycor() >= 280:
        player1.refresh()
        for i in range(0, 16):
            lista[i].faster()

        score.addscore()
        score.score()

    screen.update()
    for i in range(0,16):
        lista[i].move()
        lista[i].refresh()

    for i in range(0,16):
        if lista[i].xcor()+15 >= player1.xcor() >= lista[i].xcor()-25 and lista[i].ycor()+15 >= player1.ycor() >= lista[i].ycor()-15:
            score.over()
            game = False

screen.exitonclick()


