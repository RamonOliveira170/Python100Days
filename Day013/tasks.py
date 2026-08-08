import random
import maths


def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it!")

my_function()

dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = random.randint(1, 6)
print(dice_images[dice_num])

try:
    age = int(input("How old are you?: "))
except ValueError:
    print("You have typed in a an invalid number. Please try again with a numerical response such as 26")

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
