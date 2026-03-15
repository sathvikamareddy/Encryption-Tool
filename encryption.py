import random
import string

character = " " + string.punctuation + string.ascii_letters + string.digits
character = list(character)

key = character.copy()
random.shuffle(key)

# ENCRYPT
original_text = input("ENTER THE TEXT YOU WANT TO ENCRYPT: ")
encrypt_text = ""

for letter in original_text:
    index = character.index(letter)
    encrypt_text += key[index]

print(f"Original message: {original_text}")
print(f"Encrypted message: {encrypt_text}")

# DECRYPT
encrypt_text = input("ENTER THE TEXT YOU WANT TO DECRYPT: ")
plain_text = ""

for letter in encrypt_text:
    index = key.index(letter)
    plain_text += character[index]

print(f"Encrypted message: {encrypt_text}")
print(f"Original message: {plain_text}")
