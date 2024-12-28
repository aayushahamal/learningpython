#Step 13
#The abs() function returns the absolute value of a number, which is always positive, regardless of the number sign. You will use it to check that the estimated square root is close enough to the actual value.
#Now, create an if statement to check if the absolute value of the difference between square_mid and square_target is within the specified tolerance.


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
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2
            if abs(square_mid - square_target) < tolerance :
                pass   
