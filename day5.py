# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# characters = nr_letters + nr_numbers + nr_symbols
# sequence = ""

# l = 0
# s = 0
# n = 0

# for i in range(0, characters):
#     character_type = random.randint(1, 3)
#     if character_type == 1 and l < nr_letters:
#         letter = random.randint(0, len(letters)-1)
#         sequence += (letters[letter])
#         l += 1
#     elif character_type == 2 and s < nr_symbols:
#         symbol = random.randint(0, len(symbols)-1)  
#         sequence += (symbols[symbol])  
#         s += 1
#     elif character_type == 3 and n < nr_numbers:
#         number = random.randint(0, len(numbers)-1)
#         sequence += (numbers[number])
#         n += 1
       


# print(sequence)        

import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Calculate the total length of the password
total_length = nr_letters + nr_symbols + nr_numbers

# Create a list to store the characters for the password
password_characters = []

# Add required letters
for _ in range(nr_letters):
    password_characters.append(random.choice(letters))

# Add required symbols
for _ in range(nr_symbols):
    password_characters.append(random.choice(symbols))

# Add required numbers
for _ in range(nr_numbers):
    password_characters.append(random.choice(numbers))

# Shuffle the characters to make it random
random.shuffle(password_characters)

# Convert the list to a string
password = ''.join(password_characters)

print("Your password is:", password)
