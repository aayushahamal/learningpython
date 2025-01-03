#Inside the loop, use the addition assignment operator to add a random character from all_characters to the current value of password. 
#Use the choice() function from the secrets module for that.

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
    for i in range(length):
        password += secrets.choice(all_characters)
