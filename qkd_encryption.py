import random

def generate_key(length):
    # Generate a random key of specified length
    key = [random.choice([0, 1]) for _ in range(length)]
    return key

def xor_binary_strings(str1, str2):
    # XOR operation between two binary strings
    result = ""
    for bit1, bit2 in zip(str1, str2):
        result += str(int(bit1) ^ int(bit2))
    return result

def encrypt_message(message, key):
    # Convert message and key to binary strings
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_key = ''.join(map(str, key))

    # Perform XOR operation between message and key
    encrypted_binary = xor_binary_strings(binary_message, binary_key)

    # Convert encrypted binary back to characters
    encrypted_message = ''.join(chr(int(encrypted_binary[i:i+8], 2)) for i in range(0, len(encrypted_binary), 8))
    return encrypted_message

def decrypt_message(encrypted_message, key):
    # Convert encrypted message and key to binary strings
    binary_encrypted_message = ''.join(format(ord(char), '08b') for char in encrypted_message)
    binary_key = ''.join(map(str, key))

    # Perform XOR operation between encrypted message and key
    decrypted_binary = xor_binary_strings(binary_encrypted_message, binary_key)

    # Convert decrypted binary back to characters
    decrypted_message = ''.join(chr(int(decrypted_binary[i:i+8], 2)) for i in range(0, len(decrypted_binary), 8))
    return decrypted_message

# Message to encrypt
message = "thank you qubit by qubit for this amazing learning"

# Generate a key using QKD (for simplicity, we'll just generate a random key)
key_length = len(''.join(format(ord(char), '08b') for char in message))
key = generate_key(key_length)

# Encrypt the message
encrypted = encrypt_message(message, key)
print("Encrypted message:", encrypted)

# Decrypt the message
decrypted = decrypt_message(encrypted, key)
print("Decrypted message:", decrypted)
