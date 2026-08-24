import turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-220, 260)
        self.level = 1
        self.write_scoreboard()

    def write_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write_scoreboard()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)
