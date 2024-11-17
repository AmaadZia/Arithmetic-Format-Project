def arithmetic_arranger(problems, show_answers=False):
    """
    Arranges a list of arithmetic problems in a vertically aligned format.
    
    Parameters:
        problems (list): A list of arithmetic problems as strings (e.g., "32 + 698").
        show_answers (bool): Whether to include the answers in the output (default: False).

    Returns:
        str: The formatted arithmetic problems or an error message if input validation fails.
    """

    # Step 1: Check if the number of problems exceeds the limit
    if len(problems) > 5:
        return "Error: Too many problems."

    # Step 2: Parse operators and validate them
    operators = []  
    for problem in problems:
        parts = problem.split()
        operators.append(parts[1])
    
    for operator in operators:
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

    # Step 3: Extract numbers and validate them
    numbers = []
    for problem in problems:
        parts = problem.split()
        numbers.append(parts[0])
        numbers.append(parts[2])
    
    for number in numbers:
        if not number.isdigit():
            return "Error: Numbers must only contain digits."
        elif len(number) > 4:
            return "Error: Numbers cannot be more than four digits."

    # Step 4: Initialize rows for formatting
    answers = []
    top_row = ''
    bottom_row = ''
    answer_row = ''
    dashes = ''

    # Step 5: Process each problem and calculate results
    for i in range(0, len(numbers), 2):
        num1 = int(numbers[i])
        num2 = int(numbers[i + 1])
        operator = operators[i // 2]

        # Calculate the result
        result = num1 + num2 if operator == '+' else num1 - num2
        answers.append(result)

        # Determine spacing for alignment
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2

        # Build each row of the problem
        top_row += numbers[i].rjust(space_width)
        bottom_row += operator + numbers[i + 1].rjust(space_width - 1)
        dashes += '-' * space_width

        # Add spaces between problems
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            bottom_row += ' ' * 4
            dashes += ' ' * 4

    # Step 6: Add answers if requested
    for i in range(len(answers)):
        space_width = max(len(numbers[2 * i]), len(numbers[2 * i + 1])) + 2
        answer_row += str(answers[i]).rjust(space_width)
        if i != len(answers) - 1:
            answer_row += ' ' * 4

    # Step 7: Combine all rows into the final output
    if show_answers:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, answer_row))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))

    return arranged_problems

# Example usage
if __name__ == "__main__":
    # Test cases
    problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    print(arithmetic_arranger(problems, show_answers=True))
