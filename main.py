# coding=utf-8

import random

def guess_game():
    correct = False
    num_guess = 0
    print("Welcome to the guess game!")
    print("I am thinking of a number between 1-10 and you have 3 guesses to get it!")
    number = random.randint(0, 10)
    while not correct and num_guess < 3:
        guess = input("Pick a number between 1 and 10 ")
        guess = int(guess)
        if guess < number:
            print("that is too low!")
            num_guess += 1
        if guess > number:
            print("that is too high!")
            num_guess += 1
        if guess == number:
            correct = True

    if correct == False:
        print("Sorry! You are out of guesses. I was thinking of the number " + str(number) + " Better luck next time!")
    if correct == True:
        print("Correct! The number was " + str(number))

guess_game()
