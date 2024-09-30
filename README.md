HOW TO PLAY

1. Start the app
2. Enter '1' to start playing
3. Enter any button to exit the app
4. You start with a numbers round every time, so provide an expression
   for given set of numbers and check the result, get your score
5. Then it comes to the letters round, provide 10 times a letter type (vowel
   or consonant), then create the longest word for a given set of letters,
   get your score
6. Exit the program when needed, entering any button except '1', then get your
   overall score. (You cannot exit the program during the round!)
7. Enjoy!

PROGRAM FILES

1. The program has 6 files: file_processing.py, words.txt, letters_round.py,
   numbers_round.py, menu.py, main.py

2. File words.py contains all english words from the English

3. File file_processing.py has the file_reading function reads words from a file named
   words.txt and creates a dictionary where the keys are the length of the words and
   the values are lists of tuples. Each tuple contains the word in uppercase and the
   sorted list of its uppercase characters. The function skips words longer than 10
   characters and appends the word and its sorted characters to the corresponding key
   in the dictionary.

4. File menu.py contains 2 functions:
   4.1 The greeting function is displaying a welcome message for the Des Chiffres Et
   Des Letters game, prompting the user to either start the game by entering '1' or
   exit the application by entering any other button.
   4.2 The bye function is displaying a farewell message to the user. It thanks the user
   for choosing the app and expresses anticipation for their return. Additionally,
   it includes a fire emoji to add a friendly and warm touch to the goodbye message.

5. File letters_round.py contains 4 functions:
   5.1 The prompt_letter_type function is prompting the user to choose between a vowel or
   a consonant, generating a string of 10 random letters based on the user's choices,
   and returning the generated string of letters.
   5.2 The user_answer function is prompting the user to enter the longest word they
   can create from the given letters. It compares the user's input with the proper
   word that can be formed from the letters. If the user's word matches the proper word,
   it prints "Correct!". Otherwise, it informs the user about the correct word and
   its length. Finally, it returns the length of the proper word and the length of
   the user's word for scoring purposes.
   5.3 The longest_word function is responsible for finding the longest valid word that
   can be created using the given string of letters. It iterates through the words in
   the dictionary and checks if each word can be formed using the provided letters.
   It considers the frequency of each letter in the word and compares it with the
   frequency of letters in the given string. If a word can be formed, it is added to
   the list of proper words along with its length. Finally, the function returns
   the longest word that can be formed from the given letters along with its length.
   5.4 The score_letters function calculates the score based on the lengths of the
   proper word and the user's word. It takes two parameters: length_proper which
   represents the length of the proper word that can be formed from the given letters,
   and user_length which represents the length of the word entered by the user.

6. File numbers_round.py
   6.1 The target_number function generates a random integer between 100 and
   999 (inclusive) and returns this randomly generated number.
   6.2 The six_random_numbers function generates a list of 6 random numbers for use
   in the game. It includes 4 large numbers (25, 50, 75, 100) and
   2 small numbers (randomly chosen from 1 to 10). The function randomly selects
   numbers from the combined list of large and small numbers to create a list of
   6 numbers, which will be used in the game.
   6.3 The read_user_expression function is checking if the user input expression is
   valid for the game. It takes two parameters: user_expression,
   which is the expression entered by the user, and generated_arr, which is a list of
   6 randomly generated numbers.
   6.4 The expression_is_proper function is checking whether the user input expression
   is valid for the game. It evaluates the user's expression and
   compares the result with the target number. If the expression is valid and the
   result matches the target number, the function returns 1, indicating that the
   user's expression is correct. Otherwise, it returns 0. Additionally, the
   function handles exceptions like NameError or SyntaxError that may occur during
   the evaluation of the expression.
   6.5 The computer_solution function is responsible for finding a solution to
   the game given a target number and a list of 6 randomly
   generated numbers. It iterates through different combinations of numbers
   and operations to create expressions and evaluates them to check if they equal
   the target number. If a valid expression that matches the target number is found,
   it returns that expression. If no solution is found, it returns a message
   indicating that the solution does not exist.
   6.6 The score_numbers function calculates a score based on the user's expression in
   the game. It evaluates the user's expression using eval and
   compares the result with the target number. If the evaluation is successful and
   the result matches the target number, the function calculates a score by subtracting
   the absolute difference between the target number and the user's result divided
   by 10 from 100.

7. File main.py contains while in_game == '1' statement, which is creating a loop
   that will continue executing the code block (program interface) inside the loop
   as long as the value of the variable in_game is equal to the string '1'. This
   loop structure allows the player to keep playing the game rounds until they
   decide to exit by entering a different value for in_game.
