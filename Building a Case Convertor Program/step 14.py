#So far, in this project you have used a for loop to iterate over your input string and convert it into 
#the desired output. Now you'll begin the transition from a for loop to a list comprehension.
#Begin by commenting out all the lines of code inside the convert_to_snake_case() function. 
#Don't delete them as they'll be helpful when you implement the logic using a list comprehension.
#Remember to add the pass keyword to the function body to prevent the code from failing during the tests.

def convert_to_snake_case(pascal_or_camel_cased_string):
    pass
    #snake_cased_char_list = []
    #for char in pascal_or_camel_cased_string:
        #if char.isupper():
            #converted_character = '_' + char.lower()
            #snake_cased_char_list.append(converted_character)
        #else:
            #snake_cased_char_list.append(char)
    #snake_cased_string = ''.join(snake_cased_char_list)
    #clean_snake_cased_string = snake_cased_string.strip('_')

    #return clean_snake_cased_string
def main():
    print(convert_to_snake_case('aLongAndComplexString'))

main()
