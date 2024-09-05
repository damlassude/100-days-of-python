import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list=["aardvark", "baboon", "camel"]

# TODO-1 - Create a variable called 'lives' to keep track.
# Set lives to equal 6

lives=6

chosen_word=random.choice(word_list)
print(chosen_word)

placeholder=""
for letter in chosen_word:
   placeholder+="_ "
print(placeholder)

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

# TODO-2 - If guess is not correct, reduce lives by 1.
#If lives goes down to 0, the game should end.
    
    if guess not in chosen_word:
       lives-=1
       if lives==0:
           game_over=True
           print("You lose")

    if "_ " not in display:
        game_over=True
        print("You win")

# TODO-3 - Print the ASCII art

    print(stages[lives])
    