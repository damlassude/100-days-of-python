def greet():
    print("Hello")
    print("This is Damla")
    print("How are you?")
greet()
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")

x=input("What is your name? ")

greet_with_name(x)

#Functions with more than 1 input

def greet_with(name,location):
    print(f"Hello {name}. \nWhat is it like in {location}?")

greet_with("Damla","İstanbul")
    