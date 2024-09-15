from game_data import data
import random
import os

def clear():
    # Clear screen command based on the operating system
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

a=random.choice(data)
b=random.choice(data)


while a==b:
    b=random.choice(data)

score=0
while True:

    print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}.")
    print(f"Against B: {b['name']}, a {b['description']} from {b['country']}.")

    guess=input("Who has more followers? Type 'A' or 'B': ").lower()

    if (guess=="a" and a['follower_count']>b['follower_count']) or (guess=="b" and b['follower_count']>a['follower_count']):
        score+=1
        print("Correct! Current score: "+str(score))
        a=b
        b=random.choice(data)

        while b==a:
            b=random.choice(data)
        
        clear()
        print("Correct! Current score: "+str(score))
        
    else:
        clear()
        print("Wrong. Final score: "+str(score))
        break
