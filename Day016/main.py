from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    option = input(f"What would you like? {menu.get_items()}?: ").strip().lower()
    if option == "espresso" or option == "cappuccino" or option == "latte":
        selected_coffee = menu.find_drink(option)
        if coffee_maker.is_resource_sufficient(selected_coffee) and money_machine.make_payment(selected_coffee.cost):
            coffee_maker.make_coffee(selected_coffee)
    elif option == "report":
        coffee_maker.report()
        money_machine.report()
    elif option == "off":
        print("Closing...")
        is_on = False
    else:
        continue
