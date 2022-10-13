#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#If the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
for letter in chosen_word:
  display.append("_")
print(display)

guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

#Apple = 5 Letters, x - 1 for index, replace it 
#If we guess b, if b, -1, replace
count = 0

for letter in chosen_word:
    if letter == guess:
      display[count] = letter
      count += 1
    else:
        count += 1

#count_letter = len(chosen_word)
    
print(display)
