#Within the if statement body, you are going to add the converted character to the list you created earlier.
#For this, the .append() method will be used. This method adds a given object to the end of the list it is invoked on.
#Use the .append() method on the snake_cased_char_list to add the converted_character to the list.

def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
