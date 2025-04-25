from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600,height=600)

screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
score.write_score()

with open("high_score.txt", "r") as file:
    high = int(file.read())
score.high_score = high
score.reset()
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()
    if snake.lista[0].distance(food) < 15:
        food.refresh()
        score.add_points()
        score.write_score()
        snake.get_bigger()
    if snake.lista[0].xcor() > 290 or snake.lista[0].xcor() < -290 or snake.lista[0].ycor() > 290 or snake.lista[0].ycor() < -290:
        score.write_score()
        if score.high_score > high:
            with open("bin/high_score.txt", "w") as file:
                file.write(str(score.high_score))
        score.reset()
        snake.reset()
    for i in range(1,len(snake.lista) - 1):
        if snake.lista[0].distance(snake.lista[i]) < 10:
            score.write_score()
            if score.high_score > high:
                with open("bin/high_score.txt", "w") as file:
                    file.write(str(score.high_score))

            snake.reset()
            score.reset()

screen.exitonclick()