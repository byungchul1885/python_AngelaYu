import turtle
import pandas as pd
import logging as l

l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', level=l.INFO, datefmt='%I:%M:%S')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
l.info(all_states)

ok_states = []

while len(ok_states) < 50:
    answer = screen.textinput(title=f"{len(ok_states)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer == "Exit":
        missing = []
        for state in all_states:
            if state not in ok_states:
                missing.append(state)
        new_data = pd.DataFrame(missing)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer in all_states:
        ok_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
