from random import randint
DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """
    Checks if a number is prime
    """
    if num < 2 or num == 4:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True


def lets_game():
    """
    Describes the condition and the correct answer
    """
    condition = randint(1, 100)
    if is_prime(condition):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return condition, correct_answer
