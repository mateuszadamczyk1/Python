weight = int(input("What is your weight? "))
height = float(input("What is your height in meters? "))

bmi = weight / (height ** 2)

print(f"Your bmi is {bmi}")

if bmi < 18.5:
    print("You have an underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print("You have slight overweight.")
elif bmi >= 30 and bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")    