#Now, turn the empty string in the constraint tuple into a regex pattern to match a single digit. Use a character class specifying each digit from 0 to 9.

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
            (nums, '[0123456789]')
        ]        
    return password
    
# new_password = generate_password(8)
# print(new_password)

pattern = 'w[ha]'
quote = 'Not all those who wander are lost.'
# print(re.findall(pattern, quote))
