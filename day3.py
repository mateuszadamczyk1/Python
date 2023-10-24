print("Welcome to the story")

first = input("Where do you want to go? (left or right)")

if first == "right":
    print("Good choice!")
    second = input("Swim or wait? (swim or wait)")
    if second == "wait":
        print("Good choice")
        third = input("Which door? (blue, yellow or green)")
        if third == "yellow":
            print("You won!")
        else:
            print("You loose!")    
    else:
        print("You loose!")  
else:
    print("You loose!")                      