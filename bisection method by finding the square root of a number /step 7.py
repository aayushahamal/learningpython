#Create an elif statement to check if square_target is equal to 0. If it is, assign the value 0 to the root variable. Also, print the message 'The square root of {square_target} is 0'. Remember to format the message using an f-string.


def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target ==0:
        root = 0
        print(f'The square root of {square_target} is 0')
