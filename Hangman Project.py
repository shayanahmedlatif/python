# Preparing the Hangman Project
# Imported Functions
import random

# Hangmand Project
def hangman_project_fn():

    # Random list of words.
    words = ["Apple", "Banana", "Orange", "Peach", "Mango", "Sweet"]
        # Selecting random word from the list.
    random_selected_word = random.choice(words).lower()
        # Count the number of a selected word.
    count_selected_word = len(random_selected_word)
        
        # Create an empty list of "_" based on the number of characters in random_selected_word
    empty_list = ["_"] * len(random_selected_word)

    hangman_pic = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    # Tracking guessing limits
    max_guess_limit = len(random_selected_word)
    

    # While loop to ask user to input a guessed word
    while True:
            # Ask the input
            guessed_letter = input("Guess a letter: ").lower()
            # Produce error for the same guessed word
            if guessed_letter in empty_list:
                print(f"You've already guessed the letter {guessed_letter}")
                continue # if yes, it will ask again for a new letter.
            # Check the guessed letter in the select word
            if guessed_letter in random_selected_word:
                for i in range(count_selected_word):
                    if random_selected_word[i] == guessed_letter:
                        empty_list[i] = guessed_letter
                print(empty_list)
                
                if  "_" not in empty_list:
                    print("You win! " + "The correct word is " + ("".join(empty_list).capitalize()))
                    break
            else:
                if max_guess_limit > 0:
                    print(hangman_pic[len(hangman_pic) - max_guess_limit])
                    print(f"Wrong guess! You've {max_guess_limit - 1} guesses left")
                    # Decrease max_guess_limit after every two incorrect tries
                    max_guess_limit -= 1
            if max_guess_limit == 0:
                print("Limit Exceeded. Play again. The correct word was " + random_selected_word)
                break

hangman_project_fn()
