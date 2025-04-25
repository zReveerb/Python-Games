import random
import turtle
from fcntl import FASYNC
from os import MFD_ALLOW_SEALING
from turtle import Turtle, Screen

screen = Screen()
screen.listen()
red = Turtle()
green = Turtle()
blue = Turtle()
purple = Turtle()
yellow = Turtle()
orange = Turtle()
lista = [red,orange,blue,green,purple,yellow]
string = ["red", "orange", "blue", "green", "purple","yellow"]
contador = [0,0,0,0,0,0]
red.color("red")
green.color("green")
blue.color("blue")
purple.color("purple")
yellow.color("yellow")
orange.color("orange")

def shapes(listas):
    for i in range(0,6):
        listas[i].shape("turtle")
shapes(lista)

def notdraw(listas):
    for i in range(0,6):
        listas[i].penup()
notdraw(lista)

def beggining(listas):
    y = 200
    for i in range(0,6):
        listas[i].setposition(-300,y)
        y -= 75

beggining(lista)
def compara(listas):
    for i in range(0,6):
        if aleatorio == listas[i]:
            contador[i] += 1
    for j in range(0,6):
        if contador[j] >= 150:
            return False
    return True
def quem_ganhou(listas):
    for j in range(0,6):
        if contador[j] >= 150:
            return listas[j]

escolha = screen.textinput("Choice:", "Choose a color to win: 'yellow', 'blue', 'green', 'red','orange' or 'purple'!")
sem_ganhador = True
while sem_ganhador:
    aleatorio = random.choice(lista)
    aleatorio.forward(5)
    sem_ganhador = compara(lista)

if quem_ganhou(string) == escolha:
    print("Congrats, you chose the fastest turtle!")
else:
    print(f"I'm sorry, it was {quem_ganhou(string)} who won!")
screen.exitonclick()

