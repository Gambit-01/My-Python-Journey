import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

# creating a dictionary with data from the csv save into dataframe
nato_dict = {row.letter:row.code for index,row in data.iterrows()}

# Asking user for input
word = input("Please type in your word\n").upper()

# Creating the list of words according to the letters in the inputed word
phonetic_word_list = [nato_dict[letter] for letter in word]
print (phonetic_word_list)
