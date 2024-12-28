#If the square_target is less than 0, no real-valued square root can be computed. Therefore, raise a ValueError with the message 'Square root of negative number is not defined in real numbers'. 
#Don't forget to remove the pass keywor



def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
