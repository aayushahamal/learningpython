#A standalone single underscore is used to represent a value you don't care or that won't be used in your code. Your iteration variable is not actually used.
#Modify your i variable into a single underscore.

import secrets
import string


def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    password = ''
    # Generate password
    for _ in range(length):
        password += secrets.choice(all_characters)
    
