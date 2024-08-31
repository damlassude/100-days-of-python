#rock paper scissors game
import random
print("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors")
user_choice=input()
computer_choice=random.randint(0,2)
print("You chose: ")
if user_choice=="0":
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    print("Computer chose: ")
    if computer_choice==0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("It's a tie.")
       
    elif computer_choice==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("Computer wins.")
    
    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("You win.")

elif user_choice=="1":
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    print("Computer chose: ")
    if computer_choice==0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("You win.")

    elif computer_choice==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("It's a tie.")

    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("Computer wins.")

elif user_choice=="2":
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if computer_choice==0:
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        print("Computer wins.")

    elif computer_choice==1:
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        print("You win!")

    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        print("It's a tie.")

else:
    print("Game over.")



"""
this version is way better

import random

# Seçeneklerin tanımlanması
choices = [
    ""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"", 
    ""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"",
    ""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""
]

# Oyun sonuçlarının tanımlanması
results = {
    (0, 0): "It's a tie.",
    (0, 1): "Computer wins.",
    (0, 2): "You win.",
    (1, 0): "You win.",
    (1, 1): "It's a tie.",
    (1, 2): "Computer wins.",
    (2, 0): "Computer wins.",
    (2, 1): "You win!",
    (2, 2): "It's a tie."
}

# Kullanıcı ve bilgisayar seçimleri
print("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors")
user_choice = int(input())
computer_choice = random.randint(0, 2)

# Seçimlerin gösterilmesi
print("You chose:")
print(choices[user_choice])

print("Computer chose:")
print(choices[computer_choice])

# Sonucun gösterilmesi
print(results[(user_choice, computer_choice)])
"""