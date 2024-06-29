from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def calculate(operation, first_operand, second_operand):
    """
    Addition, subtraction or multiplication of numbers
    """
    if operation == '+':
        return str(first_operand + second_operand)
    elif operation == '-':
        return str(first_operand - second_operand)
    else:
        return str(first_operand * second_operand)


def get_round():
    """
    Describes the condition and the correct answer
    """
    first_operand = randint(1, 100)
    second_operand = randint(1, 100)
    list_of_operations = '+-*'
    operation = choice(list_of_operations)
    condition = f'{str(first_operand)} {operation} {str(second_operand)}'
    correct_answer = calculate(operation, first_operand, second_operand)
    return condition, correct_answer
