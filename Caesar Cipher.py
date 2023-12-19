
# Imported functions
import string 
import math
import pyperclip
# Gathering all alphabets and numbers
all_alphabets = list(string.ascii_letters)
all_numbers = list(string.digits)


# Welcome Message!
print("Welcome to the Python decryption.")

# Defining Functions
def encryption_fn(input_text, shift_number):
    # A function to shift chars based on shift number.
    # This functions supports Alphabets and Numbers

    encrypted_text = input_text
    en_shift_num = shift_number
    # A new var for encrypted value.
    final_encrypted_text = ""
    # A for loop for shifting character based on shift number.
    for character in encrypted_text:
        # Check that if the character is a alphabet word or not.
        if character.isalpha():
            # Check if the word is uppercase if yes, return True otherwise False.
            it_is_upper = character.isupper()
            # Now shift character here based on the shift number
            shifted_character = chr((ord(character) + shift_number - ord('A' if it_is_upper else 'a')) % 26 + ord('A' if it_is_upper else 'a'))
            final_encrypted_text += shifted_character
        elif character.isnumeric():
            # if_it_is_numeric = character.isnumeric()
            shifted_character = chr((ord(character) + en_shift_num - ord('0')) % 10 + ord('0'))
            final_encrypted_text += shifted_character
            # If there is any other letter in the  encrypted_text, will return it as same
        else:
            final_encrypted_text += character
    return final_encrypted_text

def decryption_fn(input_text, shift_number):
#  A function to revers the chars based on the shift number.
# This functions supports Alphabets and Numbers
    decrypted_text = input_text
    de_shift_num = shift_number
    # A new var for reverse-shifted text
    final_decrypted_text = ""
    # A loop to shift a character reverse back to it's original posistion
    for character in decrypted_text:
        if character.isalpha():
            # Check if there is any UPPERCASE letter
            it_is_upper = character.isupper()
            # Reverse back the character  to the original one based on the correct shift number
            reversed_shifted = chr((ord(character) - shift_number - ord('A' if it_is_upper else 'a') + 26) % 26 + ord('A' if it_is_upper else 'a'))
            # Assigns the character to it's position back
            final_decrypted_text += reversed_shifted
        elif character.isnumeric():
            # if_it_is_numeric =  character.isnumeric()
            reversed_shifted = chr((ord(character) - de_shift_num - ord('0') + 10) % 10 + ord('0'))
            final_decrypted_text += reversed_shifted
        else:
            final_decrypted_text += character
    return final_decrypted_text

def astrisks_fn(input_text):
#  This fn combine all alphabets into '*' sign and leave spaces.
    astrisks_word = []
    # Capture each word from input_text
    for each_word in input_text.split():
        # Check if they are alphabets
        if each_word.isalpha():
            # Add * sign equal to the lenght of each word e.g. abs == ***
            astrisks_word.append('*' * len(each_word))
        else:
            # Return as same char if not alphabetic
            astrisks_word.append(each_word)
    # Join them to make a new sentence or word.
    return ' '.join(astrisks_word)


#  A while loop to continues itetrating the above functions until exit.

while True:
    greet_input = input("Type 'encode' to encrypt or 'decode' to decrypt or type 'exit' to cancel. ").lower()

    # Exits the program
    if greet_input == "exit":
        print("Exiting the program, goodbye.")
        break
    # Set input_text and shift_num for encryption or decryption based on choice
    if greet_input == "encode" or greet_input == "decode":
        input_text = input("Enter your text here: ")
        while True:
            try:
                # Takes the input in number, convert to float and then round it up.
                shift_number = math.ceil(float(input("Enter your desired shift number: ")))
                # Use the sum of all alphabets and numbers to set max shift range.
                if shift_number <= len(all_alphabets + all_numbers):
                # Sets input for encryption
                    if greet_input == "encode":
                        text_results = encryption_fn(input_text, shift_number)
                        cvrt_astrisks_word = astrisks_fn(input_text)
                    elif greet_input == "decode":
                        text_results = decryption_fn(input_text, shift_number)
                    while True:
                        # An input to ask user if they want to copy the results.
                        copy_message = input("Do you want to copy the results? Y or N ").lower()
                        # Condition to figure out input
                        if copy_message == "y":
                            # Copy when user type y in the input field.
                            pyperclip.copy(text_results)
                            print(f"Result copied")
                            print(f"You encrypted text is {cvrt_astrisks_word}")
                            break
                        # Print the result on screen.
                        elif copy_message == "n":
                            print(f"Sure! see the results below.")
                            print(f"Your {'encrypted' if greet_input == 'encode' else 'decrypted'} text is' {text_results}', and your Shift code is '{shift_number}'.")
                            break
                        else:
                            print(f"Please type 'Y' or 'N'.")
                            continue
                    break
                else:
                    print(f"Max range occured, Try again.")
            except ValueError:
                print("Invalid number, please try again.") 
    else:
        print(f"Wrong choice try again.")
        continue
    prompt_message = input(f"Do you restart the Encryption or Decryption process? Type 'Y' or 'N'").lower()
    if prompt_message == "y":
        continue
    else:
        break