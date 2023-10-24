import random

print("Welcome to the number guessing app")
print("The task is to guess the number between 1 and 100")
difficulty = input("Choose the difficulty level: easy or hard ").lower()

number_to_guess = random.randint(1, 100)

def play_game():
    if difficulty == "easy":
        attemp_number = 10
    else:
        attemp_number = 5

    game = True

    while game and attemp_number > 0:
        user_guess = int(input("Guess the number: "))

        if user_guess > number_to_guess:
            print("Too high")
            print("Guess again")
            attemp_number -= 1
            print(f"You have {attemp_number} attemps left")
            if attemp_number == 0:
                game = False
                print("You lose")
                print(f"The number you were looking for was {number_to_guess}")  
        elif user_guess < number_to_guess:
            print("Too low")
            print("Guess again")  
            attemp_number -= 1
            print(f"You have {attemp_number} attemps left")
            if attemp_number == 0:
                game = False
                print("You lose") 
                print(f"The number you were looking for was {number_to_guess}")   
        elif user_guess == number_to_guess:
            game = False
            print("You win!")

play_game()                