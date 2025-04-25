import turtle
import pandas
from mako.util import to_list

from Name import Name
screen = turtle.Screen()
screen.title("US States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
estados = data["state"]
estados = estados.to_list()

contador = 0
row = data[data["state"] == "Ohio"]
x = row.x
x = x.to_list()
name = Name()

while contador < 50:
    state = screen.textinput(f"Guess the state:{contador}/50","What's another state's name? ")

    for i in estados:
        if i.lower() == state.lower():
            estados.remove(i)
            contador += 1
            state = state.title()
            name.write(state)

if contador == 50:
    print("Congrats, you won!")

else:
    print("Study more and try AGAIN!")