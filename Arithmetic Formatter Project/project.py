def arithmetic_arranger(problems, display_answers=False):
    # Check if the number of problems exceeds the limit
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Lists to store parts of the arranged output
    top_row = []      # Holds the first number (operand1)
    bottom_row = []   # Holds the operator and second number (operand2)
    separator_row = []# Holds the dashes
    solution_row = [] # Holds the results (if display_answers=True)
    
    # Loop through each arithmetic problem
    for problem in problems:
        elements = problem.split()  # Split the problem into parts (e.g., ['32', '+', '8'])
        
        # Check if the format is valid (should have exactly 3 parts)
        if len(elements) != 3:
            return 'Error: Invalid format.'
        
        operand1, operator, operand2 = elements  # Assign parts to variables
        
        # Validate the operator (must be '+' or '-')
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Ensure operands only contain digits
        if not (operand1.isdigit() and operand2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check if operands are within the 4-digit limit
        if len(operand1) > 4 or len(operand2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Calculate the width of the problem (largest operand + 2 spaces)
        problem_width = max(len(operand1), len(operand2)) + 2
        
        # Format and append each part to the appropriate list
        top_row.append(operand1.rjust(problem_width))  # Right-align first operand
        bottom_row.append(operator + operand2.rjust(problem_width - 1))  # Align operator with second operand
        separator_row.append('-' * problem_width)  # Create dashes the same width as the problem
        
        # If answers need to be displayed, calculate and format the result
        if display_answers:
            if operator == '+':
                answer = str(int(operand1) + int(operand2))
            else:
                answer = str(int(operand1) - int(operand2))
            solution_row.append(answer.rjust(problem_width))  # Right-align the answer
    
    # Join each row with four spaces between problems
    arranged_problems = '    '.join(top_row) + '\n'
    arranged_problems += '    '.join(bottom_row) + '\n'
    arranged_problems += '    '.join(separator_row)
    
    # If answers need to be displayed, add them to the output
    if display_answers:
        arranged_problems += '\n' + '    '.join(solution_row)
    
    return arranged_problems

# Example usage:
print(arithmetic_arranger(["48 + 8", "1 - 3765", "9999 + 9999", "523 - 79"], True))
