#The choice() function from the random module takes a sequence and returns a random item of the sequence.
#Modify your print() call to use the choice() function and pass all_characters as the argument.

import random
import string


# Define the possible characters for the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# Combine all characters
all_characters = letters + digits + symbols

print(all_characters)
print(random.choice(all_characters))
