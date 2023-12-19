import sys
import random
import time


#  Default variables
game_finish = False
player_bank_amount = 32758434
game_rounds = 1
name = ""
player_wins = 0
dealer_wins = 0  

# All Functions
# A function to get the card value
def get_card_value(card):
    if card in ['J', 'Q', 'K']: # Check if the card matches.
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card) # Convert all other values into integer.
#returns card
# A function to get the hand value
def get_hand_value(hand):
    num_of_aces = hand.count('A') # Count 'A' in value
    value = sum([get_card_value(card) for card in hand]) # generate sum of the values by using the get_card_funciton
    while value > 21 and num_of_aces:
        value -= 10 # removes 10 if 'A' found
        num_of_aces -= 1 # reduce the iteration by 1 everytime until 0
    return value
#return value
# A function to generate segments of player bank amount
def get_amount_seg(amount):
    inc_for_segs = 1 / 4 # = 0.25 getting four increments of the entire amount
    n_of_segs = [inc_for_segs * i for i in range(1, 5)] # 0.25 * 1, 0.25 * 2 until range
    seg_in_amount = [each_segs * amount for each_segs in n_of_segs ] # 0.25 * amount(100 or anyone)
    seg_in_percentage = [each_segs * 100 for each_segs in n_of_segs] # $250 of $1000 etc.
    seg_list_values = f"{' '.join(map(str,{f'{each_seg:.0f}%'  for each_seg in seg_in_percentage}))}" # Generate simple list assigning '%' after each 
                                                                                                      # segment and join them with a space
    return seg_in_amount, seg_in_percentage, seg_list_values
#return seg_in_amount, seg_in_percentage
# A function to calculate the user balance
def calc_user_balance(amount):
    segment_amount, segment_percentage, percetage_list = get_amount_seg(amount)
    input_amt = int(input(f"What is your bet amount? {percetage_list}: "))
    while True:
        if input_amt in [100, 75, 50, 25]:
            selected_amount = int((input_amt / 100) * amount)
            pending_balance = amount - selected_amount
            return selected_amount, pending_balance
        else:
            print(f"Wrong amount. Try again.")
            continue
# returns selected_amount, pending_balance
# A function to display deck processing time
def deck_countdown(name, seconds):
    for countdown in range(seconds, 0, -1):
        sys.stdout.write(f"{name} is shuffling within {seconds}.") # display the name and time in seconds of the current player.
        sys.stdout.flush() # clear the current line
        time.sleep(1) # Once second to update current line.
        sys.stdout.write('\r' + ' ' * 50 + '\r') # clear the entire line.
        seconds -= 1 # reduce the seconds by increment of 1.
# takes two arguments name, and seconds
# This function will print the welcome message
def greeting_message():
    if game_rounds <= 1:
        print(f"Welcome to the BlackJack Game!")
        print(f"Round {game_rounds}")
    if game_rounds > 1:
        print(f"Welcome back again!")
        print(f"Round {game_rounds}")
# Ask for player name

while game_finish is not True:
    player_turn = True
    dealer_turn = True
    # Welcome Message
    greeting_message()
    amount = player_bank_amount #setting amount as player_bank_amount
    seg_in_amount, seg_in_percentage, seg_list_values = get_amount_seg(amount)
    bet_amount, balance = calc_user_balance(amount)
    print(f"Bet selected: ${bet_amount:,.2f}, Balance: ${balance:,.2f}")
    cards_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K'] * 4 # generate the same list 4 times.
    random.shuffle(cards_list) # Randomize the character of the list.
    if game_rounds <= 1:
        name = input(f"What is your name? ").capitalize()
    else:
        name
    deck_countdown(name, 3) # Time for shuffling
    player_hand = [cards_list.pop(), cards_list.pop()] # Generating and removing random values
    print(f"{name} selected: {' '.join(map(str, player_hand))} Total: {get_hand_value(player_hand)}")

    deck_countdown("Dealer", 3)
    dealer_hand = [cards_list.pop(), cards_list.pop()]
    print(f"Dealer selected: {' '.join(map(str, dealer_hand))} Total: {get_hand_value(dealer_hand)}")
    
    # Player updates if required.
    while player_turn:
        while get_hand_value(player_hand) <= 21: # While loop iterates until 21 
            ask_user = input(f"Do you want to hit or stand? ").lower()
            if ask_user == "hit":
                deck_countdown(name, 3)
                player_hand.append(cards_list.pop())
                print(f"{name} selected: {' '.join(map(str, player_hand))} Total: {get_hand_value(player_hand)}")
            else:
                break
        player_turn = False
    # Dealer updates if required
    while dealer_turn:
        while get_hand_value(dealer_hand) <= 21:
            deck_countdown("Dealer", 3)
            dealer_hand.append(cards_list.pop())
        print(f"Dealer selected: {' '.join(map(str, dealer_hand))} Total: {get_hand_value(dealer_hand)}")
        dealer_turn = False
    # Program's condition start here.
    if get_hand_value(player_hand) > 21 and get_hand_value(dealer_hand) > 21:
        player_turn = False
        dealer_turn = False
        print(f"It's a draw")
        player_wins += 0
        dealer_wins += 0
        game_rounds +=1
        game_finish = False
    elif get_hand_value(player_hand) > 21:
        player_turn = False
        print(f"{name} busts, Dealer won.")
        dealer_wins += 1
        player_wins += 0
        player_bank_amount -= bet_amount
        if input(f"Would you like to play again? Y/N ").lower() not in ['yes', 'y']:
            game_finish = True
        else:
            game_rounds += 1
            game_finish = False
    elif get_hand_value(dealer_hand) > 21:
        print(f"Dealer busts, {name} won.")
        player_bank_amount += bet_amount
        player_wins += 1
        dealer_wins += 0
        if input(f"Would you like to play again? Y/N ").lower() not in ['yes', 'y']:
            game_finish = True
        else:
            game_rounds += 1
            game_finish = False
    elif get_hand_value(dealer_hand) == 21 and len(dealer_hand) == 2:
        print("Dealer has Blackjack!")
        dealer_turn = False
        player_turn = False
        dealer_wins += 1
        player_wins += 0
        game_rounds += 1
        player_bank_amount -= bet_amount
        game_finish = False
    elif get_hand_value(player_hand) == 21 and len(player_hand) == 2:
        print(f"{name} has Blackjack!")
        player_turn = False
        dealer_turn = False
        dealer_wins += 0
        player_wins += 1
        game_rounds += 1
        player_bank_amount += bet_amount
        game_finish = False
    elif get_hand_value(player_hand) == 21:
        player_turn = False
        print(f"{name} won.")
        player_wins += 1
        dealer_wins += 0
        if input(f"Would you like to play again? Y/N ").lower() not in ['yes', 'y']:
            game_finish = True
        else:
            game_rounds += 1
            game_finish = False
    elif get_hand_value(dealer_hand) == 21:
        print(f"Dealer won.")
        dealer_turn = False
        player_bank_amount -= bet_amount
        dealer_wins += 1
        player_wins += 0
        if input(f"Would you like to play again with dealer? Y/N ").lower() not in ['yes', 'y']:
            game_finish = True
        else:
            game_rounds += 1
            game_finish = False
    elif get_hand_value(player_hand) == get_hand_value(dealer_hand):

        player_turn = False
        dealer_turn = False
        print(f"It's a draw")
        player_wins += 0
        dealer_wins += 0
        game_rounds += 1
        game_finish = False
    # Program's condition ends here.
        
else:
    # Breaks main loop
    print(f"Game over!")
    print(f"The total round in this game was {game_rounds}")
    print(f"Total wins {name}: {player_wins} Dealer wins {dealer_wins}")
    game_finish = True