from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def get_progression(len_of_list, element, step):
    """
    Get an arithmetic progression
    """
    progression = [str(element)]
    for i in range(len_of_list - 1):
        element += step
        progression.append(str(element))
    return progression


def get_round():
    """
    Describes the condition and the correct answer
    """
    element = randint(1, 100)
    step = randint(1, 10)
    len_of_list = randint(5, 10)
    position = randint(1, len_of_list)
    progression = get_progression(len_of_list, element, step)
    correct_answer = progression[position - 1]
    progression[position - 1] = '..'
    condition = ' '.join(progression)
    return condition, correct_answer
