#Now you'll repeatedly narrow down the interval by finding the midpoint of the current interval and comparing the square of the midpoint with the target value.
#For that, inside the else block, create a for loop that runs up to max_iterations times.
#For your loop, use the range function, which generates a sequence of numbers you can iterate over. The syntax is range(start, stop, step), where start is the starting integer (inclusive), stop is the last integer (not inclusive), and step is the difference between a number and the previous one in the sequence.
#Also, use _ as a loop variable. The _ acts as a placeholder and is useful when you need to use a variable but don't actually need its value.


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
            pass
