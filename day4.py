import random

choice = int(input("What do you choose? 1 - rock, 2 - paper, 3 - scissors "))

if choice < 1 or choice > 3:
    print("You chose the wrong number!")
    exit()

figures = ["ROCK", "PAPER", "SCISSORS"]

print("You chose: ")
 
print(figures[choice - 1])

computer_choice = random.randint(1, 3)

print("Computer chose: ")

print(figures[computer_choice - 1])  

if computer_choice == choice:
    print("It's a draw")
elif computer_choice == 1 and choice == 2:
    print("You win!")    
elif computer_choice == 1 and choice == 3:
    print("You lose!")  
elif computer_choice == 2 and choice == 3:
    print("You win!")    
elif computer_choice == 2 and choice == 1:
    print("You lose!")   
elif computer_choice == 3 and choice == 1:
    print("You win!")    
elif computer_choice == 3 and choice == 2:
    print("You lose!")   
else:
    print("Something went wrong :/")            

