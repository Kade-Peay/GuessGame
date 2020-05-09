#!/usr/bin/env python3
import random

arr = ['a','b','c','d','e','f','g', 'h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
r = random.randint(1,26)


def Guess(wrong):
    guess = input('Take a guess from a-z: ')
    guess.lower()

    if wrong >= 2:
        print('You ran out of guesses')
    else:
        if guess == str(arr[r]):
            print('You guessed correctly')
        else:
            print('You guessed...poorly')
            Guess(wrong + 1)


if __name__ == "__main__":
    Guess(0)