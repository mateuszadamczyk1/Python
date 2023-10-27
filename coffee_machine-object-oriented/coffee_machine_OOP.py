from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



running = True

while running:
    options = menu.get_items()
    choice = input(f"What would you like to drink? ({options}) ")

    if choice == "off":
        is_on = False
        exit()
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                print("Not enough money")
        else:
            print("There is no resources to make the drink")




