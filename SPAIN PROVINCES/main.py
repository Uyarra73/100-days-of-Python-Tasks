import turtle
import pandas


FONT = ("Courier", 10, "bold")

screen = turtle.Screen()
screen.title("SPAIN PROVINCES")
image = "blank_spain_provinces.gif"
screen.addshape(image)
turtle.shape(image)

states_list = pandas.read_csv("50_states.csv")

state_name = turtle.Turtle()
state_name.hideturtle()
state_name.penup()
state_name.color("black")
game_is_on = True
score = 0
guessed_states = []
states_to_learn = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State!  {score}/50", prompt="Write the name of a state").title()
    matching_state = states_list[states_list["state"] == answer_state]

    if answer_state == "Exit":
        for state in states_list.state:
            if state not in guessed_states:
                states_to_learn.append(state)
        study_list = pandas.DataFrame(states_to_learn)
        study_list.to_csv("states_to_learn.csv")
        break

    if not matching_state.empty:
        score += 1
        guessed_states.append(answer_state)
        x_cor = int(matching_state["x"].values[0])
        y_cor = int(matching_state["y"].values[0])
        state_name.goto(x_cor, y_cor)
        state_name.write(matching_state["state"].values[0], align="center", font=FONT)
    else:
        game_is_on = False


