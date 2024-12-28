#In Python, the is keyword checks for object identity. It's used to determine if two variables point to the same object in memory. In contrast to is, the equality operator (==) determines if the values of two objects are the same, regardless of whether they are the same object in memory.
#Outside the for loop, create an if statement to check if root is None. If it is, print the message 'Failed to converge within {max_iterations} iterations.'. Remember to format the message using an f-string.



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

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")      
