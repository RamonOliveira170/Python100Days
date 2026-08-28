import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

'''def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()'''
data = pandas.read_csv("./50_states.csv")
all_states = data["state"].to_list()

guessed_states = []

while len(guessed_states) < len(data):
    answer = screen.textinput(title=f"{len(guessed_states)}/{len(data)} Guess the State",
                              prompt="What's another State's name?").strip().title()

    if answer in all_states:
        guessed_states.append(answer)
        state_info = data[data.state == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_info.x.item(), state_info.y.item())
        t.write(answer)

    if answer == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        '''for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)'''
        st_learn = pandas.DataFrame(states_to_learn)
        st_learn.to_csv("states_to_learn.csv")

        break
