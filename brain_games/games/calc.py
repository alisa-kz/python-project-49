#!/usr/bin/env python3


from random import randint, choice


def lets_game():
    first_operand = randint(1, 100)
    second_operand = randint(1, 100)
    list_of_operations = '+-*'
    operation = choice(list_of_operations)
    condition = f'{str(first_operand)} {operation} {str(second_operand)}'
    if operation == '+':
        correct_answer = str(first_operand + second_operand)
    elif operation == '-':
        correct_answer = str(first_operand - second_operand)
    else:
        correct_answer = str(first_operand * second_operand)
    return condition, correct_answer


def description():
    return 'What is the result of the expression?'


def main():
    lets_game()


if __name__ == '__main__':
    main()

