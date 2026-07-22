print(len("Hello"))

print("Hello"[-1])

print(type(123), type("hello"), type(False), type(3.14))

print(len(str(123)))
print(len(str(False)))

print("Number of letters in your name: " + str(len(input("Enter your name: "))))

print("My age " + str(98))

print(123 + 456)
print(89 - 33)
print(3 * 9)
print(5 / 3)
print(16 // 4)
print(2 ** 3)

# PEMDAS
# () Parenthesis
# ** Exponents
# *  Multiplication
# /  Division
# +  Addiction
# -  Subtraction

height = 1.65
weight = 65

bmi = weight / (height ** 2)

print(round(bmi, 2))

score = 0

score += 1

print("Score: " + str(score))

# F-Strings

print(f"Score: {score}")