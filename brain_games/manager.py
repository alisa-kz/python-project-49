#!/usr/bin/env python3


import prompt
from brain_games import cli


def manage_game(module):
    name = cli.welcome_user()
    print(module.description())
    num_of_inputs = 3
    for i in range(num_of_inputs):
        module.lets_game()
        condition, correct_answer = module.lets_game()
        print(f'Question: {condition}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Cor"
                  f"rect answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
    return


def main():
    manage_game()


if __name__ == '__main__':
    main()
