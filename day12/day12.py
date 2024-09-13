#number guessing game

import random
number=random.randint(1,100)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty=='easy':
    attempts=10
else:
    attempts=5

for i in range (attempts):
    print(f"You have {attempts-i} attempts left")
    guess=int(input("Make a guess: "))
    if guess==number:
        print(f"You got it. The answer was {number}")
        break
    elif guess<number:
        print("Too low.")

    else:
        print("Too high.")
    
else:
    print(f"You've run out of guesses. The number was {number}.")    