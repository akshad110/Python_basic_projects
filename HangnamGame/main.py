import random
import stages_file
lives = 6
word =""
word_list = ['apple','mango','orange','papaya','cricket','football','goa','mumbai','love']
chosen_word = random.choice(word_list)

display = []
for i in range(len(chosen_word)):
    display += '_'

game_over = False
while not game_over :
    guess_letter = input("Guess a letter of the word: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess_letter:
          display[position] = guess_letter
    print(display)

    if guess_letter not in chosen_word:
        lives -= 1
        if lives == 0:
           game_over = True
           print("you lose!!")
    if '_' not in display:
        game_over = True
        print("you win!!")
        for char in chosen_word:
            word += char
        print(f"The word was: {word}")
    print(stages_file.stages[lives])



