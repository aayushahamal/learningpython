#Inside the if statement body, you need to convert any uppercase character to lowercase and prepend an underscore to this lowercase character.
#Use the .lower() string method to convert uppercase characters to lowercase characters. Then, prepend an underscore to the character. Assign the results to a variable named converted_character.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character='_'+char.lower()
