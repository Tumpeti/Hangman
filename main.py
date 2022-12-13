import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()


word = ""
for letter in range(0, len(chosen_word)):
    if chosen_word[letter] == guess:
        word += guess
    elif guess != chosen_word[letter]:  #akár else:
        word += "_"
print(word)
