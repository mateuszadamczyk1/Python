import random

word_list = ["pencil", "computer", "dishwasher"]

chosen_word = word_list[random.randint(0, len(word_list)-1)]
length = int(len(chosen_word))

to_guess = []
stages = ["1", "2", "3", "4", "5", "6"]
lives = 6

for i in range(0, length):
    to_guess += "_"

print(chosen_word)
print(to_guess)

while "_" in to_guess:
    guess = str(input("Parse in your guess: ")).lower()

    if guess in to_guess:
        print("You've already guessed this letter")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            to_guess[position] = letter 
            print(stages[lives-1])    

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])     
    print(to_guess)

    if lives == 0:
        print("You lose")
        exit()
    
else:
    print("You win!")    
   