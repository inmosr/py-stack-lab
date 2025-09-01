import art

print(art.logo)



def caesar(direction,original_text,shift_amount):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    if direction == 'decode':
        shift_amount *= -1
    output = ''
    for letter in original_text:
        if letter in alphabet:
            output += alphabet[(alphabet.index(letter) + shift_amount) % len(alphabet)]
        else:
            output += letter
    return output


while 1:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    print(caesar(direction,text,shift))
    exit = ''
    while 1:
        exit = input('Would you like to encode/decode a text again?y/n ')
        if exit == 'y':
            break
        elif exit == 'n':
            break
        else:
            print('Invalid option')
    if exit == 'n':
        break



