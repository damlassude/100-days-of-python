import random

word_list=["aardvark", "baboon", "camel"]

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder=""
for letter in chosen_word:
   placeholder+="_ "
print(placeholder)



# TODO-1 -Use a while loop to let the user guess again. 
game_over=False

correct_letters=[]

while not game_over:
    guess=input("Guess a letter: ").lower()
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

    if "_ " not in display:
        game_over=True
        print("You win")



# TODO-2 - Change the for loop so that you keep the previous correct letters in display.

    