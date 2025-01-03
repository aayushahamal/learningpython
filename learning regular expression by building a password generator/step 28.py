#The compile() function from the re module compiles the string passed as the argument into a regular expression object that can be used by other re methods.

#Declare a new pattern variable and assign the value of re.compile('i') to this variable.

import re
import secrets
import string


def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, '')
        ]        

    return password

# new_password = generate_password(8)
# print(new_password)
pattern = re.compile('i')
