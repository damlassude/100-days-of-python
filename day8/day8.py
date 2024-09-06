#caesar cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(original_text,shift_amount):

    cipher_text=""
    for letter in original_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=(position+shift_amount)%len(alphabet)
            new_letter=alphabet[new_position]
            cipher_text+=new_letter
        else:
            cipher_text+=letter
    print("Here is the encoded result: "+cipher_text)


def decrypt(cipher_text,shift_amount):

    plain_text=""
    for letter in cipher_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=(position-shift_amount)%len(alphabet)
            new_letter=alphabet[new_position]
            plain_text+=new_letter
        else:
            plain_text+=letter
    print("Here is the decoded result: "+plain_text)


def caesar(direction, text, shift):
    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)

should_continue=True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text,shift)
    restart=input("Type 'yes' to restart the game. Type 'no' to end.").lower()
    if restart=="no":
        should_continue=False
        print("Goodbye")


