from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# test = Menu()
# print(test.get_items())
money_machine = MoneyMachine()
CoffeeMaker = CoffeeMaker()
menu_machcine = Menu()
money_machine.report()
is_on = True
while is_on:
    options = menu_machcine.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        CoffeeMaker.report()
        money_machine.report()
    else:
        drink = menu_machcine.find_drink(choice)
        ask = CoffeeMaker.is_resource_sufficient(drink)
        if ask:
            if money_machine.make_payment(drink.cost):
              CoffeeMaker.make_coffee(drink)