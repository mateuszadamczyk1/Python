print("Welcome to the tip calculator")

total = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

if tip == 12:
    total = total * 1.12
    bill = total/people
    print(f"Each person have to pay {bill}")
elif tip == 15:    
    total = total * 1.15
    bill = total/people
    print(f"Each person have to pay {bill}")
elif tip == 10:   
    total = total * 1.1
    bill = total / people
    print(f"Each person have to pay {bill}")