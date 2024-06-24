#!/usr/bin/env python3


from random import randint


def is_prime(num):
    if num < 2 or num == 4:
        return 'no'
    for i in range(2, num // 2):
        if num % i == 0:
            return 'no'
    return 'yes'


def lets_game():
    condition = randint(1, 100)
    correct_answer = is_prime(condition)
    return condition, correct_answer


def description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    lets_game()


if __name__ == '__main__':
    main()
