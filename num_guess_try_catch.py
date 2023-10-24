#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Oct. 24, 2023
# This program generates a number between 0-9 and the user must guess the number and it will say if they're correct or incorrect.
# It will also be within a try catch to prevent crashing and to tell the user if they entered something other than an integer.

import random


def main():
    # get user guess
    user_guess = input("Please enter a number between 0-9: ")

    # generate random number
    correct_answer = random.randint(1, 9)

    # try converting user guess into an integer
    try:
        user_guess_as_int = int(user_guess)
        if correct_answer == user_guess_as_int:
            print("\nYou guessed correctly!")
        else:
            print("\nYou guessed incorrectly, the number was {}".format(correct_answer))
    
    # if user guess is not an integer it will tell the user
    except Exception:
        print("{} is not a number between 0 and 9.".format(user_guess))
    
    # always print a message at the end of the program
    finally:
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
