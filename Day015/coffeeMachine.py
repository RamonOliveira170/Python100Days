import menu
resources = {"water": 3000, "milk": 2000, "coffee": 1000, "money": 0}

def is_sufficient(selected_coffee):
    for item in selected_coffee["ingredients"]:
        if selected_coffee["ingredients"][item] > resources[item]:
            print(f"Not enough {item}")
            return False
    return True


def coins_calculator(coffee_cost):
    quarters = int(input("How many quarters?(0.25): ")) * 0.25
    dimes = int(input("How many dimes?(0.10): ")) * 0.10
    nickels = int(input("How many nickels?(0.05): ")) * 0.05
    penny = int(input("How many pennies?(0.01): ")) * 0.01
    money_received = quarters + dimes + nickels + penny

    if money_received < coffee_cost:
        print("\n" * 20)
        print("Please insert more coins\n")
        print(f"Here's your money {round(money_received, 2)}$\n")
        return 0
    else:
        money_received -= coffee_cost
        print(f"Here's your change {round(money_received, 2)}$\n")
        return coffee_cost


def make_coffee(operation):
    selected_coffee = menu.MENU[operation]
    if is_sufficient(selected_coffee):
        print(f"{operation} costs {selected_coffee["cost"]}$")
        money = coins_calculator(selected_coffee["cost"])
        if money > 0:
            for item in selected_coffee["ingredients"]:
                resources[item] -= selected_coffee["ingredients"][item]
            resources["money"] += selected_coffee["cost"]
            print(f"Here's your {operation} ☕\n")
    return 0


def coffee_machine():
    running = True

    while running:
        operation = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        if operation == "latte" or operation == "espresso" or operation == "cappuccino":
            make_coffee(operation)

        elif operation == "report":
            print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g "
                  f"\nMoney: {resources["money"]}$")

        elif operation == "close":
            running = False

        else:
            continue

    print("Closing...")


coffee_machine()
