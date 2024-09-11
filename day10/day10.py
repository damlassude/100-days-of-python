#calculator program
from art import logo
import os
def clear():
    # Clear screen command based on the operating system
    if os.name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

print(logo)
def calculator():

    operations={
        '+': add,
        '-':subtract,
        '*': multiply,
        '/': divide  
    }

    continue_calculating=True


    number1=float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)

    while continue_calculating:
        operation=input("Pick an operation:")
        number2=float(input("What is the second number?: "))
        result=operations[operation](number1,number2)
        print(result)

        choice=input(f"Type 'y' to continue calculating with {result},type 'n' to start a new calculation or type 'e' to exit ").lower()

        if choice=='y':
            number1=result

        elif choice=='e':
            continue_calculating=False
            print("Goodbye.")

        elif choice=='n':
            clear()
            calculator()

        else:
            print("Invalid response. Goodbye.")
            continue_calculating=False

calculator()