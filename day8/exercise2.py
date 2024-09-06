alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


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

# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text,shift_amount):

# TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
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

# TODO-3:Combine the functions into a single function called caesar().
#Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. 

def caesar(direction, text, shift):
    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)

# def caesar(direction,text,shift):
#     if direction=="decode":
#         shift_amount*=-1
#     for letter in...

caesar(direction,text,shift)


