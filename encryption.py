import random
import string

# Character set
characters = " " + string.punctuation + string.ascii_letters + string.digits
characters = list(characters)

# Generate shuffled key
key = characters.copy()
random.shuffle(key)

def encrypt(text):
    encrypted_text = ""

    for letter in text:
        index = characters.index(letter)
        encrypted_text += key[index]

    return encrypted_text


def decrypt(text):
    decrypted_text = ""

    for letter in text:
        index = key.index(letter)
        decrypted_text += characters[index]

    return decrypted_text


print("------ TEXT ENCRYPTION TOOL ------")

original_text = input("Enter text to encrypt: ")

encrypted = encrypt(original_text)
print(f"\nEncrypted Message: {encrypted}")

decrypted = decrypt(encrypted)
print(f"Decrypted Message: {decrypted}")
