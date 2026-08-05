import logo
running = True


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print(logo.logo)

number1 = float(input("What's the first number?: "))
result = 0

while running:

    operator = input("Pick an operation: \"+\" \"-\" \"*\" \"/\": ").strip()

    number2 = float(input("What's the second number?: "))

    calc_dict = {"+": add,
                 "-": subtract,
                 "*": multiply,
                 "/": divide,
    }

    result = calc_dict[operator](number1, number2)

    print(f"Result: {number1} {operator} {number2} = {result}")

    close_calc = input(f"Type 'y' to continue, calculating with the result of: \"{result}\""
                       f", type 'n' to start a new calculation or 'c' to close the program: ").lower()

    if close_calc == "n":
        print("\n" * 20)
        number1 = float(input("What's the first number?: "))
        result = 0
    elif close_calc == "y":
        print(f"The first number is {result}")
        number1 = result
    else:
        print("Closing...")
        running = False
