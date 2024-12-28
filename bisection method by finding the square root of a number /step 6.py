#If the square_target is equal to 1, declare a variable root and assign it the value 1 . Also, print the message 'The square root of {square_target} is 1'. Remember to format the message using an f-string.


def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    
