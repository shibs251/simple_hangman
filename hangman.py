#imported modules
import random
import time

#variables
words = ["apple", 'bananna', 'pear', 'mango', 'grapes', 'kiwi', 'peach']
chosen_word = random.choice(words)
word_length = str(len(chosen_word))


print('Hello, lets play a game of hangman.')
time.sleep(3)
print("Just so you know, the word you need to guess has " + word_length + " letters.")
guess = input("Guess a letter \n").lower()

print("guess " + guess + "\nchosen word " + chosen_word)
if guess in chosen_word:
    print("Yo Adrien, I did it!")
else:
    print("Try again")
