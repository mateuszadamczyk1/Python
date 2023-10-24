import day8art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(day8art.logo)

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""

#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is: {cipher_text}")    


# def decrypt(plain_text, shift_amount):
#     cipher_text = ""

#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is: {cipher_text}")    

# if direction == "encrypt":
#     encrypt(plain_text= text, shift_amount= shift) 
# elif direction == "decrypt":
#     decrypt(plain_text= text, shift_amount= shift) 

def ceasar(plain_text, shift_amount, direction):
    cipher_text = ""

    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encrypt":
                new_position = position + shift_amount
            elif direction == "decrypt":
                new_position = position - shift_amount    
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            print("Only accepts letters, not able to encrypt")
            exit()    
    print(f"The {direction}ed text is: {cipher_text}") 


should_continue = True

while should_continue:
    direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    if shift > 26:
        shift = shift % 26

    ceasar(plain_text = text, shift_amount = shift, direction = direction)  

    restart = input("Do you want to continue using this programme? (Yes or No)").lower()  

    if restart == "yes":
        should_continue = True
    elif restart == "no":
        should_continue = False
        print("Goodbye")
        exit()
    else:
        exit()        