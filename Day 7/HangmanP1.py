import random

word_list = ["aardvark", "baboon", "camel"]

def search(letter, word_list):
    if letter in word_list:
      print("Correct")
    else:
      print("Incorrect")
    

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list).lower()

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Print results of guesses

# need to check characters one by one
# store character in array, loop user input and compare
random_word = []

chosen_word.split()
for char in chosen_word:
  random_word.append(char)

print("Guess what letters are in this word: ")

for user_input in range(0, 7):
  user = input()
  search(user, random_word)


