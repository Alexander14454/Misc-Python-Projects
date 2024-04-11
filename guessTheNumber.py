#guess the number.py
#import random
import random

#generate random number
randomInt = random.randint(1 , 10)
# first guess 
print("Guess a number from 1 to 10:")
guessCount = 1
guess = input()
guess = int(guess)
# if statement incase the first guess was right
if guess == randomInt and guessCount == 1:
    print("\nYou got it your first try!!!")
else:
    mainBoolean = 'False'
    while mainBoolean == 'False':
        if guess < randomInt:
            print("\nToo low, try again")
            guess = input()
            guess = int(guess)
            guessCount += 1
        elif guess > randomInt:
            print("\nToo high, try again")
            guess = input()
            guess = int(guess)
            guessCount += 1
        elif guess == randomInt:
            print("You guess the correct answer, it took you", guessCount, "guesses to get it right." )
            mainBoolean = 'True'          