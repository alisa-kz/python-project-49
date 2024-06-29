from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def calc_gcd(first_num, second_num):
    """
    Find greatest common divisior of numbers
    """
    while first_num > 0 and second_num > 0:
        if first_num >= second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
    return max(first_num, second_num)


def get_round():
    """
    Describes the condition and the correct answer
    """
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    condition = f'{first_num} {second_num}'
    correct_answer = str(calc_gcd(first_num, second_num))
    return condition, correct_answer
