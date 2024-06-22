#!/usr/bin/env python3


from random import randint


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    return 'no'


def description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def lets_game():
    condition = randint(1, 100)
    correct_answer = is_even(condition)
    return condition, correct_answer


def main():
    lets_game()


if __name__ == '__main__':
    main()
