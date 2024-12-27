#Now, right after the for loop, use the .join() method to join the elements in snake_cased_char_list 
#using an empty string as the separator. Assign the result to a new variable named snake_cased_string.



def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    for char in pascal_or_camel_cased_string:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_cased_char_list.append(converted_character)
        else:
            snake_cased_char_list.append(char)
    snake_cased_string =''.join(snake_cased_char_list)
