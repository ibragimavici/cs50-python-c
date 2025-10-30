from random import choice
import sys

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        print("", end="")


numbers = []
numbers = range(1, level + 1)
randomchoice = choice(numbers)



while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0 and isinstance(guess, int):
            if guess == randomchoice:
                print("Just right!")
                sys.exit()
            elif guess > randomchoice:
                print("Too large!")

            elif guess < randomchoice:
                print("Too small!")



    except ValueError:
        print("", end="")


