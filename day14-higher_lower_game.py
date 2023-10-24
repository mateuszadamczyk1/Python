import random
import day14_art
import day14_data

a = "a"
b = "b"

points = 0

def answer(first_person, second_person):
    if first_person['follower_count'] > second_person['follower_count']:
        return a
    else:
        return b    
   

def answer_checker(first_person, second_person):
    global points
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    right_answer = answer(first_person, second_person)
    if guess == right_answer:
        points += 1
        print(f"Your score is: {points}")
        return True
    else:
        print(f"You lose with {points}")  
        return False
    
def change(first_person, second_person):
    swap = answer(first_person, second_person) 
    if swap == b:
        return second_person, first_person
    elif swap == a:
        return first_person, second_person
    else:
        return first_person, second_person       


def play():

    game = True

    first_person = random.choice(day14_data.data)

    while game:
        second_person = random.choice(day14_data.data)

        print(day14_art.logo)
        print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
        print(day14_art.vs)
        print(f"Compare B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")

        game = answer_checker(first_person, second_person)
        first_person, second_person = change(first_person, second_person)


play()        