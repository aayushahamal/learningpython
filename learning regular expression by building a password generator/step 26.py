#Your constraints list is going to store tuples. The first item of each tuple will be a constraint parameter.
#Modify the constraints list assignment by adding a tuple to your list. Use nums as the first item and an empty string as the second item.

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
        constraints = [(nums,'')]
        
    return password

# new_password = generate_password(8)
# print(new_password)
