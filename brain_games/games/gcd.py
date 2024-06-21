#!/usr/bin/env python3


from random import randint


def lets_game():
    first_num = randint(1, 100)
    second_num = randint(1, 100)
    condition = f'{first_num} {second_num}'
    while first_num > 0 and second_num > 0:
        if first_num >= second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
    correct_answer = str(max(first_num, second_num))
    return condition, correct_answer


def description():
    return 'Find the greatest common divisor of given numbers.'


def main():
    lets_game()


if __name__ == '__main__':
    main()
