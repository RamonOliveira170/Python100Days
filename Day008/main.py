def greet():
    print("Hello")
    print("how do you do?")
    print("Isn't the weather nice?")

greet()

# Functions that allows for inputs

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how do you do {name}?")
    print("Isn't the weather nice?")

greet_with_name("oliver")


def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52

    print(f"You have {weeks_remaining} weeks left.")


life_in_weeks(70)
