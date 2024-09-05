import random

word_list=["aardvark", "baboon", "camel"]

chosen_word=random.choice(word_list)
print(chosen_word)

# TODO-1 - Create a placeholder with the same number of blanks with the chosen_word

placeholder=""
for letter in chosen_word:
   placeholder+="_ "
print(placeholder)

guess=input("Guess a letter: ").lower()


# TODO-2 - Create a "display" that puts the guess letter in the right positions.

display=""
for i in chosen_word:
    if i==guess:
        display+=i+" "
    else:
        display+="_ "
print(display)