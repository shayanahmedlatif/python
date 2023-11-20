import random

print(f"Welcome to the RCP Game!")

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
# Scissor
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#  Ask & Validate user input
valid_choices = [0, 1, 2]
while True:
    welcome_question = input("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: ")
    try:
        welcome_question = int(welcome_question)

    except ValueError:
        print("Invalid input. Please enter a number between 0 and 2.")
        continue

    if welcome_question not in valid_choices:
        print("Invalid choice. Please enter 0, 1, or 2.")
        continue

    break

# This section decides the ASCII icon based on the selection.
selection_value = ""
if welcome_question == 0:
    selection_value = rock
elif welcome_question == 1:
    selection_value = paper
else:
    selection_value = scissor

# Combine above symbol into list
rock_paper_scissor = [rock, paper, scissor]

# Randomizing list values
random_choice_value = random.randrange(len(rock_paper_scissor))

# Selecting random choice based on random_choice_value
random_choice_selection = rock_paper_scissor[random_choice_value]

# Determine the outcome of the game
if welcome_question == 0 and random_choice_selection == scissor:
    print(f"You win! because you chose:\n {rock} \nand Computer selected:\n {scissor}")
elif welcome_question == 2 and random_choice_selection == paper:
    print(f"You win! because you chose:\n {scissor} \nand Computer selected:\n {paper}")
elif welcome_question == 1 and random_choice_selection == rock:
    print(f"You win! because you chose:\n {paper} \nand Computer selected:\n {rock}")
elif welcome_question == random_choice_value:
    print(f"It's a draw. Try again. You chose:\n{selection_value} \nand computer chose:\n{random_choice_selection}")
else:
    print(f"Computer wins! because you selected:\n {selection_value} \nand Computer chose:\n {random_choice_selection}")
