import random
import hangman_lists
from hangman_lists import logo, stages

print(logo)
chosen_word = random.choice(hangman_lists.word_list)
print(chosen_word)
word_lenght = len(chosen_word)
lives = 6
display = []
for _ in chosen_word:
    display += "_"
print(f"{' '.join(display)}")
end_of_game = False


while not end_of_game:
    guess = input("Tippelj egy betűt: ").lower()
    if guess in display:
        print("Ezt a betűt már írtad!")
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f'A(z) "{guess}" betű nincs benne a szóban, vesztettél egy életet.')

    print(display)
    print(stages[lives])
    if lives == 0:
        end_of_game = True
        print("Vesztettél!")
        print(f"A szó: {chosen_word} \nA te tippeid: {' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("Győztél!")
        print(f"{' '.join(display)}")
