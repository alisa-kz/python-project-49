from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """
    Checks if a number is even
    """
    if num % 2 == 0:
        return True
    return False


def get_round():
    """
    Describes the condition and the correct answer
    """
    condition = randint(1, 100)
    if is_even(condition):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return condition, correct_answer
