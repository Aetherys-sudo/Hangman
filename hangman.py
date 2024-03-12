# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import re

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    counter = 0
    for char in secret_word:
      if char in letters_guessed:
        counter += 1
    
    if counter == len(secret_word):
      return True
    else:
      return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"'
    guessed_word = ""
    for char in secret_word:
      if char in letters_guessed:
        guessed_word = guessed_word + char
      else:
        guessed_word = guessed_word + '_ '

    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    remaining_letters = ""
    for char in all_letters:
      if char not in letters_guessed:
         remaining_letters += char
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return remaining_letters
    
def check_new_letter(secret_word, new_letter):
  if new_letter in secret_word:
    return get_guessed_word(secret_word, new_letter)
  else:
    return None

def get_unique_letters(secret_word):
  return set(secret_word)



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Initialize general variables
    guesses = 6
    warnings = 3
    letters_guessed = []

    # Print initial welcome message
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("------------------------")

    # Check if we still have guesses and if we still haven't guessed the word
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):

      # Print recurring messages for each guessing round
      print(f"You have {guesses} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")

      # Get the letter from the user
      new_letter = input("Please guess a letter: ")

      # Check if it is a valid letter and subtract either a warning (if any are left), or a guess if the user doesn't enter the correct input
      if not str.isalpha(new_letter) or len(new_letter) > 1:
        if warnings > 0:
          warnings -= 1
          print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        else:
          guesses -= 1
          print(f"Oops! That is not a valid letter. You have 0 warnings left, so you lost a guess instead, you now have {guesses} guesses: {get_guessed_word(secret_word, letters_guessed)}")
      
      # If the letter entered has already been guessed, subtract either a warning (if any left), or a guess
      if new_letter not in get_available_letters(letters_guessed):
        if warnings > 0:
          warnings -= 1
          print(f"Oops! You've already guessed that letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        else:
          guesses -= 1
          print(f"Oops! That is not a valid letter. You have 0 warnings left, so you lost a guess instead, you now have {guesses} guesses: {get_guessed_word(secret_word, letters_guessed)}")

      # Convert the input to lowercase and use it like this, regardless of the user input
      new_letter = str.lower(new_letter)

      # Check if the letter is part of the word, and if not, subtract either one guess (for consonants) or two guessses (for vowels)
      if check_new_letter(secret_word, new_letter) == None:
        if new_letter in "aeiou":
          guesses -= 2
        else:
          guesses -= 1
        
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
      else:
        # If the letter is in the word, get the rest of the unused letters, update the word with the given letter, and add the guessed letter to the guessed letters list
        remaining_letters = get_available_letters(letters_guessed)
        guessed_word = get_guessed_word(secret_word, new_letter)
        letters_guessed.append(new_letter)

        # Check if the word has been guessed and compute the total score and leave the game loop
        if is_word_guessed(secret_word, letters_guessed) == True:
          total_score = guesses * len(get_unique_letters(secret_word))
          print("Congratulations, you won!")
          print("Your total score for this game is:", total_score)
          break
        else:
          # If the game is still not over, let the user know that their word was good and show the updated word
          print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
          print("------------------------")
      
      # If the user lost because they don't have any more guesses, show them the word and end the game
      if guesses == 0:
        print("------------------------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")







# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # Remove any white spaces in the word that has the missing letters
    my_word = my_word.replace(" ", "")

    # Check that the words have the same length
    if len(my_word) == len(other_word):
      # Iterate over every character of both words
      for i in range(0, len(my_word)):
        # If the letters are not matching, check if we have an underscore instead
        if my_word[i] != other_word[i] and my_word[i] != '_':
          # If the characters are different and we don't have the underscore in the first word, this means that the words are not matching
          return False
        elif my_word[i] == '_':
            # When we do have an underscore in the first word, check if the letter in the second word appears in the word more than once, and since the underscore would represent that letter, check if we have 0 occurences in the first word
          if other_word.count(other_word[i]) > 1 and my_word.count(other_word[i]) > 0:
              return False

    else:
      return False
    
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # Format the word and remove white spaces
    formatted_word = ""
    my_word = my_word.replace(" ", "")

    # Gets the letters in the word and adds them to a string
    for char in my_word:
      if char != '_':
        formatted_word += char
    
    # Gets the unique letters in the string that we got at the previous step
    unique_letters = get_unique_letters(formatted_word)

    # Generate a regex pattern containing the whole lowercase alphabet
    regex_pattern = "["+string.ascii_lowercase+"]"

    # Remove the unique letters obtained at the previous step from the regex pattern, in order to have the pattern match only non-existing letters
    for el in unique_letters:
      regex_pattern = regex_pattern.replace(str(el), "")

    # Generate the full regex pattern, where we insert either the existing letter, or the pattern from the previous step if we have an underscore, so we can match all valid letters
    full_pattern = "^"
    for char in my_word:
      if char == '_':
        full_pattern += regex_pattern
      else:
        full_pattern += char
    
    full_pattern += "$"
    print(full_pattern)
    # Get the list of matches if found and return it
    matches = []
    for word in wordlist:
      match = re.match(full_pattern, word, flags=re.I)
      if match != None:
        matches.append(match.group())
    
    return matches

    
      
      



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # Initialize general variables
    guesses = 6
    warnings = 3
    letters_guessed = []

    # Print initial welcome message
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("------------------------")

    # Check if we still have guesses and if we still haven't guessed the word
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):

      # Print recurring messages for each guessing round
      print(f"You have {guesses} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")

      # Get the letter from the user
      new_letter = input("Please guess a letter: ")

      # Check if it is a valid letter and subtract either a warning (if any are left), or a guess if the user doesn't enter the correct input
      if len(new_letter) > 1:
        if warnings > 0:
          warnings -= 1
          print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        else:
          guesses -= 1
          print(f"Oops! That is not a valid letter. You have 0 warnings left, so you lost a guess instead, you now have {guesses} guesses: {get_guessed_word(secret_word, letters_guessed)}")
      
      if not str.isalpha(new_letter):
        if new_letter != "*":
          if warnings > 0:
            warnings -= 1
            print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
          else:
            guesses -= 1
            print(f"Oops! That is not a valid letter. You have 0 warnings left, so you lost a guess instead, you now have {guesses} guesses: {get_guessed_word(secret_word, letters_guessed)}")
      
      # Check if the user's input was an *, and print the hints without penalizing them
      if new_letter == "*":
        print("Possible word matches are:")
        print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        print("------------------------")

      # If the letter entered has already been guessed, subtract either a warning (if any left), or a guess
      if new_letter not in get_available_letters(letters_guessed) and new_letter != "*":
        if warnings > 0:
          warnings -= 1
          print(f"Oops! You've already guessed that letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
        else:
          guesses -= 1
          print(f"Oops! That is not a valid letter. You have 0 warnings left, so you lost a guess instead, you now have {guesses} guesses: {get_guessed_word(secret_word, letters_guessed)}")

      # Convert the input to lowercase and use it like this, regardless of the user input
      new_letter = str.lower(new_letter)

      # Check if the letter is part of the word, and if not, subtract either one guess (for consonants) or two guessses (for vowels)
      if check_new_letter(secret_word, new_letter) == None and new_letter != "*":
        if new_letter in "aeiou":
          guesses -= 2
        else:
          guesses -= 1
        
        print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
      else:
        # If the letter is in the word, get the rest of the unused letters, update the word with the given letter, and add the guessed letter to the guessed letters list
        remaining_letters = get_available_letters(letters_guessed)
        guessed_word = get_guessed_word(secret_word, new_letter)
        letters_guessed.append(new_letter)

        # Check if the word has been guessed and compute the total score and leave the game loop
        if is_word_guessed(secret_word, letters_guessed) == True:
          total_score = guesses * len(get_unique_letters(secret_word))
          print("Congratulations, you won!")
          print("Your total score for this game is:", total_score)
          break
        else:
          # If the game is still not over, let the user know that their word was good and show the updated word
          print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
          print("------------------------")
      
      # If the user lost because they don't have any more guesses, show them the word and end the game
      if guesses == 0:
        print("------------------------")
        print(f"Sorry, you ran out of guesses. The word was {secret_word}.")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    secret_word = "apple"
    hangman_with_hints(secret_word)
