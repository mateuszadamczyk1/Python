size = input("What do you want the pizza size to be? (S, M, L)? ")
pepperoni = input("Do you want pepperoni? (Y or N)")   
cheese = input("Do you want extra cheese? (Y or N)")

if size == "S":
    bill = 18
elif size == "M":
    bill = 20
else:
    bill = 25


if size == "S" and pepperoni == "Y":
    bill += 2    
elif size == "M" or size =="L" and pepperoni == "Y":
    bill += 3 

if cheese == "Y":
    bill += 1

print(f"Your bill is {bill}")   