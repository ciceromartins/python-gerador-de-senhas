import random
import string

def generatePassword(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

print(generatePassword()) # Tamanho: 12 caracteres
print(generatePassword(16)) # Tamanho: 16 caracteres
print(generatePassword(6)) # Tamanho: 6 caracteres