#Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

should_continue = True

num1 = float(input("What is the first number? "))

while should_continue:

    for key in operations:
        print(key)

    operation_symbol = input("Pick the operation from the options above. ")    

    num2 = float(input("What is the second number? "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    restart = input("Do you want to continue with another operation? (Yes or No)").lower()  

    if restart == "yes":
        should_continue = True
        num1 = answer
    elif restart == "no":
        should_continue = False
        print("Goodbye")
        exit()
    else:
        exit()

