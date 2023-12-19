import random

cards_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K'] * 4
random.shuffle(cards_list)
print(cards_list)