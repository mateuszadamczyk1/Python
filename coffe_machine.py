MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

case = ""

def check_resources(case):
    if MENU[case]["ingredients"]["water"] > resources["water"]:
        print("Not enough water, sorry!")
        exit()
    elif MENU[case]["ingredients"]["milk"] > resources["milk"]:
        print("Not enough milk, sorry!")
        exit()
    elif MENU[case]["ingredients"]["coffee"] > resources["coffee"]:
        print("Not enough coffee, sorry!")
        exit()
    else:
        print("...")


def check_resources_for_espresso(case):
    if MENU[case]["ingredients"]["water"] > resources["water"]:
        print("Not enough water, sorry!")
        exit()
    elif MENU[case]["ingredients"]["coffee"] > resources["coffee"]:
        print("Not enough coffee, sorry!")
        exit()
    else:
        print("...")


def check_coins():
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    sum = quarters + dimes + nickles + pennies
    return sum


def is_possible_to_serve(case, quantity):
    if quantity >= MENU[case]["cost"]:
        print("On it")
        resources["water"] = resources["water"] - MENU[case]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[case]["ingredients"]["coffee"]
        change = quantity - MENU[case]["cost"]
        change = round(change, 2)
        resources["money"] += MENU[case]["cost"]
        print("Enjoy your drink!")
        if change > 0:
            print(f"Here's your change: {change}")
    elif quantity < MENU[case]["cost"]:
        print("Not enough money, returning.")
        exit()


def what_to_drink():
    order = input("What would you like? (espresso, latte, cappuccino): ").lower()
    return order



def coffee_machine():
    running = True

    while running:

        case = what_to_drink()
        if case == "espresso":
            check_resources_for_espresso(case)
            print("The cost is: ",MENU["espresso"]["cost"])
            print("Insert coins")
            quantity = check_coins()
            is_possible_to_serve(case, quantity)
        elif case == "latte":
            check_resources(case)
            print("The cost is: ",MENU["latte"]["cost"])
            print("Insert coins")
            quantity = check_coins()
            is_possible_to_serve(case, quantity)
            resources["milk"] = resources["milk"] - MENU[case]["ingredients"]["milk"]
        elif case == "cappuccino":
            check_resources(case)
            print("The cost is: ",MENU["cappuccino"]["cost"])
            print("Insert coins")
            quantity = check_coins()
            is_possible_to_serve(case, quantity)
            resources["milk"] = resources["milk"] - MENU[case]["ingredients"]["milk"]
        elif case == "report":
            for key in resources:
                print(key + ":", resources[key])
        elif case == "off":
            print("Turning off...")
            exit()

        run_again = input("Do you want to order again? (Y or N) ").lower()

        if run_again == "y":
            running = True
        else:
            running = False
            exit()


coffee_machine()