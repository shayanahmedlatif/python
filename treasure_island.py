# This image below is implemented via https://ascii.co.uk/
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to the treasure Island,\nYour mission is to find treasure\n")
cross_road_question = input(f'''You're at a cross road. Where do you want to go? Type "left" or "right"\n''').lower()
if cross_road_question == "left":
    question_swim_wait = input(f'''You've come to a lake. There is an island in the middle of the lake. 
Type "wait" to wait for a boat. Type "swim" to swim across. ''').lower()
    if question_swim_wait == "wait":
        which_door_question = input(f'''You arrive at the island unharmed. 
There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ''').lower()
        if which_door_question == "yellow":
            print(f"You found the treasure. You Win!")
        if which_door_question == "red":
            print(f"Burned by fire. Game Over.")
        if which_door_question == "blue":
            print(f"Eaten by beasts. Game Over.")
        else:
            print(f"Game Over.")
    else: 
        print(f"Attack by trout. Game Over.")
else:
    print(f"Fall into a hole. Game over.")