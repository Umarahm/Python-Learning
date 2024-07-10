alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
        
def encrypt(plain_text, shift_amount):
    cypher_text= ""
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cypher_text += new_letter
    print(f"The Encoded Text is: {cypher_text} ")


def decrypt(cypher_text , shift_amount):
    plain_text= ""
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    for letter in cypher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The Decoded Text is: {plain_text} ")


if direction == "encode":
    encrypt(plain_text = text ,shift_amount = shift)
elif direction == "decode":
    decrypt(cypher_text = text , shift_amount = shift)
else:
    print("Wrong Input")  
