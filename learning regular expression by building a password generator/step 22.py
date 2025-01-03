#It seems all fine, but it would be nice to have a way to check that the generated password complies to specific features. 
#For example, a minimum number of special characters, digits, or uppercase/lowercase letters. You are going to take care of that very soon.

#For now, comment out the last two lines of your code.



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
    
#new_password = generate_password(8)
#print(new_password)
