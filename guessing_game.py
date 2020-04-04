"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

high_score = 12


def start_game():
    global high_score
    print('-----------------------------------')
    print('Welcome To The Number Guessing Game')
    print('-----------------------------------')
    print('Current Highscore is ' + str(high_score))
    secret_numer = (round(random.random() * 100))
    attempts = 1
    user_guess = input('Guess a number between 1 and 100: ')
    keep_looping = True

    while keep_looping:
        try:
            user_guess = int(user_guess)
            if int(user_guess) < 0 or int(user_guess) > 100:
                user_guess = input(
                    'Error - Please guess a number between 0 and 100: ')
            else:
                if int(user_guess) == secret_numer:
                    print("You guessed the correct number! It was {}. It took you {} tries.".format(
                        secret_numer, attempts))
                    if attempts < high_score:
                        print('You set a new highscore! Congrats')
                        high_score = attempts
                    try:
                        if str(input('Play again? y/N : ')).upper() == 'Y':
                            start_game()
                    except ValueError:
                        print('Exiting Game')
                    print("Exiting Game")
                    keep_looping = False
                elif int(user_guess) < secret_numer:
                    user_guess = int(input("It's higher. Guess again: "))
                    attempts += 1
                elif int(user_guess) > secret_numer:
                    user_guess = int(input("It's lower. Guess again: "))
                    attempts += 1
        except ValueError:
            user_guess = input('Error - Please enter a number: ')
            continue


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
