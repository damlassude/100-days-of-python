#hangman game
import random
from hangman_words import word_list
from hangman_art import stages

lives=6

chosen_word=random.choice(word_list)
#print(chosen_word)

placeholder=""
for letter in chosen_word:
   placeholder+="_ "
print(placeholder)

game_over=False

correct_letters=[]

while not game_over:
    guess=input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed {guess}")

    display=""
    for i in chosen_word:
        if i==guess:
            display+=i+" "
            correct_letters.append(i)
        elif i in correct_letters:
            display+=i+" " 
        else:
            display+="_ "
    print(display)

# TODO-2 - If guess is not correct, reduce lives by 1.
#If lives goes down to 0, the game should end.
    
    if guess not in chosen_word:
       lives-=1
       print("You have "+str(lives)+" lives left")
       if lives==0:
           game_over=True
           print("You lose")
           print("The word was "+chosen_word)

    if "_ " not in display:
        game_over=True
        print("You win")

# TODO-3 - Print the ASCII art

    print(stages[lives])
    