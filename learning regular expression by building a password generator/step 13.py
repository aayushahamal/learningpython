#Declare a generate_password function and write all your code except the import lines inside the function body.

import secrets
import string
def generate_password(letters, digits, symbols):
# Define the possible characters for the password
  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation

# Combine all characters
  all_characters = letters + digits + symbols

