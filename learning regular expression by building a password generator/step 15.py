#Step 15
#At the bottom of your function, declare a password variable and assign an empty string to this variable.

import secrets
import string


def generate_password(length):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols
    password =''
