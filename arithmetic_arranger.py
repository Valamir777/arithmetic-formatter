def arithmetic_arranger(problems, val=False):
    """
    :param problems: A set of mathematical problems in string form
    :param val: whether the solutions should be displayed or not.
    :return:
    """
    # Variables
    topRow = ''
    middleRow = ''
    bottomRow = ''
    numbers = []
    values = list(map(lambda x: eval(x), problems))

    # Check if quantity of problems is acceptable
    if len(problems) > 5:
        problemsArranged = 'Error: Too many problems.'
        return problemsArranged

    # check operations and create list of strings
    operations = list(map(lambda x: x.split()[1], problems))
    if not set(operations) == {'+', '-'} or not len(set(operations)) == 2:
        problemsArranged = "Error: Operator must be '+' or '-'."
        return problemsArranged

    # organize and check validity of numbers
    for number in problems:
        tempNumber = number.split()
        numbers[len(numbers):] = (tempNumber[0], tempNumber[2])

    if not all(map(lambda x: x.isdigit(), numbers)):
        arranged_problems = "Error: Numbers must only contain digits."
        return arranged_problems

    if not all(map(lambda x: len(x) < 5, numbers)):
        arranged_problems = "Error: Numbers cannot be more than four digits."
        return arranged_problems

    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i + 1])) + 2
        topRow += numbers[i].rjust(space_width)
        bottomRow += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            topRow += ' ' * 4
            bottomRow += ' ' * 4
            solutions += ' ' * 4

    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        middleRow += operations[i // 2]
        middleRow += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            middleRow += ' ' * 4

    # display true or false
    if val:
        problemsArranged = '\n'.join((topRow, middleRow, bottomRow, solutions))
    else:
        problemsArranged = '\n'.join((topRow, middleRow, bottomRow))

    return problemsArranged
