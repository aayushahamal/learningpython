#You need to handle the characters that are already in lowercase by adding them to the list of converted characters.
#Right after the if statement within the for loop, add an else clause and use the .append() method to add char to the snake_cased_char_list variable.


def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
