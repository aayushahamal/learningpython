#Inside the else clause, initialize the low variable to 0 and the high variable to be the maximum of either 1 or square_target as the square root of a number is always less than or equal to the number itself.

def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')
    else:
        low = 0
        high = max(1 , square_target)
