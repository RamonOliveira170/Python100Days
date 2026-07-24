states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"]

print(states_of_america[1])
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

states_of_america.append("New York")

print(states_of_america[-1])

states_of_america.extend(["Chicago", "Los angeles"])

print(states_of_america)
print(len(states_of_america))