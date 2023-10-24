n = int(input("Parse in the number you want to check: "))

def checker(n):
    for i in range(2, n-1):
        if n % i == 0:
            print("It's not the prime number")
            exit()
    else:
            print("It's a prime number") 

checker(n)       