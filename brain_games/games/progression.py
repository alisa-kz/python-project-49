from random import randint
DESCRIPTION = 'What number is missing in the progression?'


def find_num(len_of_list, element, step, progression, position):
    """
    Find element of progression
    """
    for i in range(len_of_list):
        element += step
        progression.append(str(element))
    return progression[position - 1]


def lets_game():
    """
    Describes the condition and the correct answer
    """
    element = randint(1, 100)
    step = randint(1, 10)
    len_of_list = randint(5, 10)
    position = randint(1, len_of_list)
    progression = []
    correct_answer = find_num(len_of_list, element, step, progression, position)
    progression[position - 1] = '..'
    condition = ' '.join(progression)
    return condition, correct_answer
