def encode_name(name):
    secret_code = ""
    for char in name:
        if char.isalpha():
            if char.islower():
                secret_code += chr(((ord(char) - ord('a') + 3) % 26) + ord('a'))
            else:
                secret_code += chr(((ord(char) - ord('A') + 3) % 26) + ord('A'))
        else:
            secret_code += char
    return secret_code

# Input your name
name = input("Enter your name: ")
encoded_name = encode_name(name)
print("Your name in secret code is:", encoded_name)
