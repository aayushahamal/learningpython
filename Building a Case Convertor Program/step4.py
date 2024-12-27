#Step 4 In both camel case and pascal case, uppercase characters mark the beginning of new words. To convert the input string to snake case, you will need to check if the characters in the input string are uppercase.
#You can use the .isupper() string method to check if a character is uppercase. This method returns True if the character is uppercase and False if it is not.
#Inside the for loop, add an if statement to check if the current character is uppercase. Move the pass statement inside the new if statement.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            pass
    
