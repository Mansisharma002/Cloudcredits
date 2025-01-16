# **with user input**

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")


# ** without user input **
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad
# from Crypto.Random import get_random_bytes
# import base64

# # Encryption function
# def encrypt(plain_text, key):
#     cipher = AES.new(key, AES.MODE_CBC)
#     ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
#     iv = base64.b64encode(cipher.iv).decode('utf-8')
#     ct = base64.b64encode(ct_bytes).decode('utf-8')
#     return iv, ct

# Decryption function
# def decrypt(iv, cipher_text, key):
#     iv = base64.b64decode(iv)
#     ct = base64.b64decode(cipher_text)
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
#     return pt

# # Generate a random AES key (16 bytes for AES-128)
# key = get_random_bytes(16)

# # Example usage
# plain_text = "Mansi!"
# iv, encrypted_text = encrypt(plain_text, key)
# decrypted_text = decrypt(iv, encrypted_text, key)

# print(f"Original Text: {plain_text}")
# print(f"Encrypted Text: {encrypted_text}")
# print(f"Decrypted Text: {decrypted_text}")
