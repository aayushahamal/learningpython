#Finally, declare a variable new_password and assign it the result of calling generate_password. 
#Pass 8 as the argument to your generate_password call.

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
        
    return password
    
new_password = generate_password(8)
