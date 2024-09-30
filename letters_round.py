from random import choice
import file_processing as words

word_dictionary = words.file_reading()

def prompt_letter_type():
  vowels = list('EYUIOA')
  consonants = list('QWRTPSDFGHJKLZXCVBNM')
  letters = 0
  answers_list = []
  string_letters = ''
  
  while letters < 10:
    ask_letter = input('\n\tWhat letter type do you want?\n\t\t1 - vowel\n\t\t2 - consonant\n')
    if ask_letter in list('12'):
      letters += 1
      answers_list.append(int(ask_letter))
    else:
      print('\n\tThis letter type does not exist, try one more time!:\n')
  
  for i in answers_list:
    if i == 1:
      string_letters += choice(vowels)
    else:
      string_letters += choice(consonants)
  
  return f'\n\tHere are your letters: {string_letters}\n', string_letters


def longest_word(string_letters : str):
  letters_list = sorted(list(string_letters))
  proper_words = []
  flag = 0
  for i in word_dictionary.items():
    for j in i[1]:
      for k in j[1]:
        if k in letters_list:
          if j[1].count(k) == letters_list.count(k):
            continue
          else:
            flag = 1
            break
        else:
          flag = 1
          break
      
      if not flag:
        proper_words.append((j[0], len(j[0])))
      
      flag = 0
  
  return sorted(proper_words, key=lambda x: x[1])[-1]


def user_answer(string_letters : str):
  proper_word, length = longest_word(string_letters)
  user_word = input('\n\tEnter the longest word you can create from given letters:\n').upper()
  if proper_word == user_word:
    print('\n\tCorrect!\n')
  else:
    print(f'\n\tNo, the correct word is {proper_word}, its length is {length}')
  
  return length, len(user_word)


def score_letters(length_proper, user_length):
  return 100 -  (length_proper - user_length) * 10
