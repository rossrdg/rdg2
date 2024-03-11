import turtle
import pandas
screen = turtle.Screen()
screen.title("50 state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer = screen.textinput(title= f"{len(guessed_states)} / 50 Correct States", prompt= "Guess a state").title()
    if answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        q = pandas.DataFrame(missing_states)
        q.to_csv("states_missed.csv")
        s = pandas.DataFrame(guessed_states)
        s.to_csv("score.csv")
        break
    if answer in all_states:
        if answer not in guessed_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer)
            guessed_states.append(answer)


turtle.mainloop()



