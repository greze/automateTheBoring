# Guess the number game
import random
secretNumber =  random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

# allow for 6 guesses
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print('Too low.')
    elif guess > secretNumber:
        print('Too high')
    else:
        break #correct answer
    
if guess == secretNumber:
    print('Way to go, champ. You guessed correctly in ' + str(guessesTaken) + ' guesses.')
else:
    print("You're not very good at guessing numbers.")