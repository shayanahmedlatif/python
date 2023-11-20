import random
print(f"Welcome the the RCP Game!")

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


# Ask user to input a value
welcome_question = input("What do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors ")
welcome_question = int(welcome_question)
selection_value = ""
# Generating values for user input
if welcome_question == 0:
    selection_value = rock
if welcome_question == 1:
    selection_value = paper
if welcome_question == 2:
    selection_value = scissor

# Combine above symbol into list
rock_paper_scissor = [rock, paper, scissor]

# Randomizing list values
random_choice_value = random.randrange(len(rock_paper_scissor))

# Selecting random choice based on random_choice_value
random_choice_selection = rock_paper_scissor[random_choice_value]

if welcome_question == 0 and random_choice_selection == scissor:
    print(f"You win! because you choose \n {rock} \nand Computer selected \n {scissor}")
elif welcome_question == 2 and random_choice_selection == paper:
    print(f"You win! because you choose \n {scissor} \nand Computer selected \n {paper}")
elif welcome_question == 1 and random_choice_selection == rock:
    print(f"You win! because you choose \n {paper} \nand Computer selected \n {rock}")
elif welcome_question == random_choice_value:
    print(f"It's a draw. Try again. You Choose \n{selection_value} \nand computer choose \n{random_choice_selection}")
else:
    print(f"Computer Win! because you selected \n {selection_value} \nand Computer choose \n {random_choice_selection}")



# print(f"You choose\n {scissor}")