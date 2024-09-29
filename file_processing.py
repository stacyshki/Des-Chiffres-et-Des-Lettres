def file_reading():
  word_dictionary = {}
  
  with open('words.txt', 'r') as file:
    
    for value in file:
      value = value[:-2]
      key = len(value)
      
      if key > 10: # as we prompt for a letter 10 times, word cant be longer
        continue
      elif key in word_dictionary.keys():
        word_dictionary[key].append((value.upper(), sorted(list(value.upper()))))
      else:
        word_dictionary[key] = [(value.upper(), sorted(list(value.upper())))]
  
  return word_dictionary