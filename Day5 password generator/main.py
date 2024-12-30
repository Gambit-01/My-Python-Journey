# # #Password Generator Project
# # import random
# # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# # symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# # print("Welcome to the PyPassword Generator!")
# # nr_letters= int(input("How many letters would you like in your password?\n")) 
# # nr_symbols = int(input(f"How many symbols would you like?\n"))
# # nr_numbers = int(input(f"How many numbers would you like?\n"))

# # passwordList = []
# # for letter in range (1,nr_letters+1):
# #     symbi = letters[random.randint(1,len(letters)-1)]
# #     passwordList.append(symbi)
# # for letter in range (1,nr_numbers+1):
# #     symbi = numbers[random.randint(1,len(numbers)-1)]
# #     passwordList.append(symbi)
# # for letter in range (1,nr_symbols+1):
# #     symbi = symbols[random.randint(1,len(symbols)-1)]
# #     passwordList.append(symbi)
# # print(passwordList)
# # random.shuffle(passwordList)
# # print(passwordList)

# # passwordY = ""
# # for letter in passwordList:
# #     passwordY += letter

# # finalPassword = (passwordY)
# # print(passwordY)


# # #Eazy Level - Order not randomised:
# # #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# # #Hard Level - Order of characters randomised:
# # #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P




# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input(" encode or decrypt").lower()
# text = input("What is the message")
# shift = int(input("What is the shift number"))
# shift = shift % 25
# print(shift)

# def encrypt(direction,text,shift):
#     message = ""
#     if direction == "encode":
#         for letter in text:
#             if letter == " ":
#                 message += " "
#             else:
#                 num = (alphabet.index(letter) + shift)%26
#                 message += alphabet[num]
#     else:
#         for letter in text:
#             if letter == " ":
#                 message += " "
#             else:
#                 num = (alphabet.index(letter) - shift)%26
#                 message += alphabet[num]
#     print(message)

# encrypt(direction,text,shift)


import random
randy = random.randint(1,101)
lives = 10

def check_guess(guessed):
    if guessed == randy:
        print ("woohoo you win")
        return True
    elif guessed < randy:
        print("You guessed low try again")
    else:
        print("You guessed higher try again later")
    return False

guessed = int(input(("I am thinking of a number between 1 and 100 can you guess it\n")))
while lives > 0:
    if check_guess(guessed):
        lives = 0
    lives -= 1
    print(f"You have {lives} remaining")
    guessed = int(input())



