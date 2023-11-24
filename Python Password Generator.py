# Imported Functions
import string
import random

# Welcome Messages
print("Welcome to the password generator.")
print("Generate strong password, Minimum length is 8 required.")


# Gathered all information 
# Like, Alphabets, Numbers, and Special Characters

all_characs = list(string.punctuation)
all_alphabets = list(string.ascii_letters)
all_nums = list(string.digits)
# print(all_characs)


# Input validation
# Ask questions and checks if they're valid integer.
# Then move to the next input/
# If not, try again to ask, and throughs an error message.

while True:
    # Default password length is 8 characters.
    password_length = input("How long would you like your password?\n") or 8
    try: 
         password_length = int(password_length)
    except:
        print("Invalid Input! Please try again!\n")
        
    # Inputs to gather user selected length in passwords.
    password_characs = input(f"How many special characters you want? You've {password_length} characters left.\n") or 4
    try:
         password_characs = int(password_characs)
    except:
        print("Invalid Input! Please try again!\n")

    if password_length < password_characs:
        print(f"Limit Exceed! You cannot choose more that {password_length} characters.  Try again")
        continue   
         
    password_alpha = input(f"How many alphabets (Captalize) you want? You've {(int(password_length) - int(password_characs))} characters left.\n") or 2
    try:
         password_alpha = int(password_alpha)
    except:
        print("Invalid Input! Please try again!\n")
    
    if password_length < password_alpha:
        print(f"Limit Exceed! You cannot choose more that {password_length} characters. Try again")
        continue  
        
    password_nums = input(f"How many numbers you want? You've {(int(password_length) -int(password_characs) - int(password_alpha))} characters left.\n") or 2
    try: 
         password_nums = int(password_nums)
    except:
        print("Invalid Input! Please try again!\n")

    if password_length < password_nums:
         print(f"Limit Exceed! You cannot choose more that {password_length} characters.  Try again")
         continue  
    

    if password_length < 8:
            print("Your password length is too short! Please try again.")
            print("The minimum length is 8 characters.")
    if password_characs +  password_alpha + password_nums > password_length or password_length < 8:
        print(f"You length exceed than {password_length}. Please try again.")
        continue
    break

# Generating information for password & converting values into strings
gen_password_characs = ((random.sample(all_characs, password_characs)))
gen_password_alpha = (random.sample(all_alphabets, password_alpha))
gen_passwords_nums = ((random.sample(all_nums, password_nums)))

# Converting a list of three variable into a single variable string.
generated_password_list = gen_password_characs + gen_password_alpha + gen_passwords_nums

# Joining & Randominzing strings
generated_password = "".join(generated_password_list)

# Convert the string to a list of characters
generated_password_list = list(generated_password)

# Shuffle the list
random.shuffle(generated_password_list)

# Convert the list back to a string
password = "".join(generated_password_list)


print(f"Here is your Generated password. {password}")