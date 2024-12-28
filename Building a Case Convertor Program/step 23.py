#Change the input string to 'IAmAPascalCasedString' and see if it comes out as 'i_am_a_pascal_cased_string', even though that's a lie.


def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

    

main()
