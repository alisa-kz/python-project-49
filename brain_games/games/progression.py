#!/usr/bin/env python3


from random import randint


def lets_game():
    element = randint(1, 100)
    step = randint(1, 10)
    length_of_progression = randint(5, 10)
    position = randint(1, length_of_progression)
    progression_list = []
    progression = ''
    for i in range(length_of_progression):
        element += step
        progression_list.append(element)
    correct_answer = str(progression_list[position - 1])
    progression_list[position - 1] = '..'
    for char in progression_list:
        progression = progression + str(char) + ' '
    condition = progression.rstrip()
    return condition, correct_answer


def description():
    return 'What number is missing in the progression?'


def main():
    lets_game()


if __name__ == '__main__':
    main()
