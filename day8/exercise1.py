alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(original_text,shift_amount):

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text
    cipher_text=""
    for letter in original_text:
        position=alphabet.index(letter)
        new_position=(position+shift_amount)%len(alphabet)
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print("Here is the encoded result: "+cipher_text)

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
    #new_position=(position+shift_amount)%len(alphabet), bc 26 letters in alphabet


# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(text,shift)