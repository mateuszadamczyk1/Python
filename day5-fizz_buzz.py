print("Welcome to fizz buzz")

limit = int(input("Parse in the range for the fizz buzz game: "))

for i in range(1, limit):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
    else:
        print(i)
i += 1                    