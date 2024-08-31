print(r"""               _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
""")
             
print("Welcome to the Treasure Island. Your mission is to find the treasure.\nYou're at a cross road. Where do you want to go?\nType 'left' or 'right' ")
direction=input().lower()
if direction=="left":
    print("You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across.")
    move=input().lower()
    if move=="wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        door=input().lower()
        if door=="yellow":
            print("You found the treasure. You win!")
        elif door=="blue":
            print("You enter a room of beasts. You lose. Game over.")
        elif door=="red":
            print("It's a room full of fire. You lose. Game over.")
        else:
            print("Game over.")
    elif move=="swim":
        print("You get attacked by an angry trout. You lose. Game over.")
    else:
        print("Game over.")
elif direction=="right":
    print("You fell into a hole. You lose. Game over.")
else:
    print("Game over.")






    