import random

logos= '''
   _____                          _   _                                     _               
  / ____|                        | | | |                                   | |              
 | |  __ _   _  ___  ___ ___     | |_| |__   ___      _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | __| '_ \ / _ \    | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |_| | | |  __/    | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/     \__|_| |_|\___|    |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
'''

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level):
    if level == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def check_answer(guessed_num,answer,attempts):
    if guessed_num < answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_num > answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is right... The answer was {answer}")

def guess_number():
    print(logos)
    print("Let me think of a number between 1 to 50: ")
    answer = random.randint(1, 50)
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("You Have entered invalid input.\nPlease choose from the above options: \n1.easy\n2.hard")
        return
    guessed_num = 0
    while guessed_num != answer:
        print(f"You have {attempts} remaining to guess the number.")
        guessed_num = int(input("Guess the number: "))
        attempts = check_answer(guessed_num, answer, attempts)
        if attempts == 0:
            print("You are out of guesses...you lose!")
            return
        elif guessed_num!=answer:
            print("Guess again.")
guess_number()

