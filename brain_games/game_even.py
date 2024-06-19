#!/usr/bin/env python3

from random import randint
import prompt
from brain_games import cli


def is_even(num):
  if num % 2 == 0:
      return 'yes'
  return 'no'


def is_even_game():
  name = cli.welcome_user()
  print('Answer "yes" if the number is even, otherwise answer "no".')
  num_of_inputs = 3
  for i in range(num_of_inputs):
      random_num = randint(1, 100)
      print(f'Question: {random_num}')
      user_answer = prompt.string('Your answer: ')
      correct_answer = is_even(random_num)
      if user_answer == correct_answer:
          print('Correct!')
      else:
          print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
          print(f"Let's try again, {name}!")
          return
  print(f'Congratulations, {name}!')
  return

def main():
    is_even_game()

if __name__ == '__main__':
    main()

