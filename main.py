import menu
import letters_round as lr
import numbers_round as nr
from time import sleep

menu.greeting()
in_game = input('\nEnter what to do:\n')
letters_score = []
numbers_score = []

while in_game == '1':
  print('\nRound 1: Numbers\n')
  target_number = nr.target_number()
  six_numbers = nr.six_random_numbers()
  print(f'\n\tGiven numbers {six_numbers}')
  print(f'\tCompute the expression to get {target_number}')
  print('\tRemember, you are allowed to use only +,-,*,//')
  user_expression = input('\tWrite your expression to get the target number or "NO" if the solution does not exist:\n\t')
  num_computer = nr.computer_solution(target_number, six_numbers)
  if num_computer != 'the solution does not exist':
    if nr.read_user_expression(user_expression, six_numbers):
      if nr.expression_is_proper(user_expression, target_number):
        print('\n\tCongratulations! The expression is correct!\n')
      else:
        print('\n\tIncorrect expression, you lose this round...\n')
    else:
      print('\n\tIncorrect expression, you lose this round...\n')
  else:
    if user_expression == 'NO':
      print('\n\tYou are correct!\n')
    else:
      print('\n\tThe solution does not exist. You are incorrect\n')
  
  print(f'\n\tThe is the computer solution: {num_computer}\n')
  sleep(2)
  score_1 = nr.score_numbers(target_number, user_expression)
  numbers_score.append(score_1)
  print(f'\nYour score in numbers round is {score_1}\n')
  
  print('\nRound 2: Letters\n')
  string, letters = lr.prompt_letter_type()
  print(string)
  correct_length, user_length = lr.user_answer(letters)
  score_2 = lr.score_letters(correct_length, user_length)
  letters_score.append(score_2)
  print(f'\nYour score in letters round is {score_2}')
  sleep(1)
  print('\nGame is over!\n')
  sleep(3)
  
  menu.greeting()
  in_game = input('\nEnter what to do:\n')

print(f'Your overall score in numbers is {sum(numbers_score)} out of {len(numbers_score) * 100}')
print(f'Your overall score in letters is {sum(letters_score)} out of {len(letters_score) * 100}')
menu.bye()
