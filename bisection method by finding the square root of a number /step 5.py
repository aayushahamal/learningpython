#You'll create separate cases for when square_target is 0 or 1.
#Begin by creating an if statement to check if square_target is equal to 1.





def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        pass    
