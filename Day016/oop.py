import turtle
import prettytable

michelangelo = turtle.Turtle()

michelangelo.shape("turtle")

michelangelo.color("orange")

michelangelo.forward(100)
michelangelo.left(120)
michelangelo.forward(100)
michelangelo.left(120)
michelangelo.forward(100)

for _ in range(5):
    michelangelo.left(60)
    michelangelo.forward(100)
    michelangelo.left(120)
    michelangelo.forward(100)
    michelangelo.left(120)
    michelangelo.forward(100)


my_screen = turtle.Screen()

my_screen.exitonclick()

table = prettytable.PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Bulbasaur", "Charmander", "Squirtle"])

table.add_column("Type", ["Electric", "Grass", "Fire", "Water"])

table.add_column("Type 2", ["None", "Poison", "None", "None"])

table.align = "l"

print(table)
