from random import randint
from itertools import product, permutations

def target_number():
  return randint(100, 999)


def six_random_numbers():
  large_numbers = [25, 50, 75, 100]
  small_numbers = [i for i in range(1, 11)]
  numbers_arr = large_numbers + small_numbers
  generated_arr = []
  
  for i in range(6):
    random_index = randint(0, len(numbers_arr)-1)
    generated_arr.append(numbers_arr[random_index])
  
  return generated_arr


def read_user_expression(user_expression: str, generated_arr : list):
  
  for i in user_expression:
    if i in ['-', '+', '//', '*', ' '] + [str(i) for i in generated_arr]:
      continue
    else:
      return 0
  
  return 1


def expression_is_proper(user_expression : str, target_number : int):
  try:
    user_number = eval(user_expression)
  except NameError or SyntaxError:
    return 0
  
  if user_number == target_number:
    return 1
  
  return 0


def computer_solution(target_number : int, generated_arr : list):
  operations = ['+', '-', '*', '//']
  
  for i in range(2,len(generated_arr)+1):
    for array in permutations(generated_arr,r=i):
      for operation_chain in product(operations, repeat=len(array)-1):
        expression = str(array[0])
        
        for operation, number in zip(operation_chain, array[1:]):
          expression += f' {operation} {number}'
        
        if eval(expression) == target_number:
          return expression
  
  return 'the solution does not exist'


def score_numbers(target_number : int, user_expression : str):
  try:
    user_number = eval(user_expression)
    return 100 - (target_number - user_number) // 10
  except NameError or SyntaxError:
    return 0
