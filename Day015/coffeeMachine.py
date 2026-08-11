import menu


def coins_calculator(coffee_cost):
    quarters = int(input("How many quarters?(0.25): ")) * 0.25
    dimes = int(input("How many dimes?(0.10): ")) * 0.10
    nickels = int(input("How many nickels?(0.05): ")) * 0.05
    penny = int(input("How many pennies?(0.01): ")) * 0.01
    coins = quarters + dimes + nickels + penny

    if coins < coffee_cost:
        print("\n" * 20)
        print("Please insert more coins\n")
        print(f"Here's your change {coins}$\n")
        return 0
    else:
        coins -= coffee_cost
        print(f"Here's your change {coins}$\n")
        return coffee_cost


def make_coffee(operation, water, milk, coffee):
    selected_coffee = menu.MENU[operation]
    if selected_coffee["ingredients"]["water"] >= water:
        print("Not enough water\n")
    elif selected_coffee["ingredients"]["coffee"] >= coffee:
        print("Not enough coffee\n")
    elif operation != "espresso" and selected_coffee["ingredients"]["milk"] >= milk:
        print("Not enough milk\n")
    else:
        print(f"{operation} costs {selected_coffee["cost"]}$")
        money = coins_calculator(selected_coffee["cost"])
        if money > 0:
            water = selected_coffee["ingredients"]["water"]
            if operation != "espresso":
                milk = selected_coffee["ingredients"]["milk"]
            else:
                milk = 0
            coffee = selected_coffee["ingredients"]["coffee"]
            return [water, milk, coffee, money]
    return [0, 0, 0, 0]


def coffee_machine():
    water = 3000
    milk = 2000
    coffee = 1000
    money = 0
    operation = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

    while operation != "close":
        if operation == "latte" or operation == "espresso" or operation == "cappuccino":
            coffee_list = make_coffee(operation, water, milk, coffee)
            water -= coffee_list[0]
            milk -= coffee_list[1]
            coffee -= coffee_list[2]
            money += coffee_list[3]
            operation = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        elif operation == "report":
            print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: {money}$")
            operation = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()

        else:
            operation = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower().strip()

    print("Closing...")


coffee_machine()
