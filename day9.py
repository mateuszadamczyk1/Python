import os
print("Anonymous auction")

bidders = {}

def add_data(name, bid):
    bidders[name] = bid

should_continue = True    

while should_continue == True:
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    add_data(name, bid)
    os.system('clear')
    cont = input("Is there any person that want to bid? (Y or N)").lower()
    if cont == "y":
        should_continue = True
    else:
        should_continue = False    
else:
    max_value = max(bidders.values()) 

    print("The winner is: ", list(bidders.keys())
      [list(bidders.values()).index(max_value)])

