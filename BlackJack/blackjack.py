# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import print_card_name, draw_card, print_header, draw_starting_hand, print_end_turn_status, print_end_game_status

# Write all of your part 4 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# USER SECTION
user_hand = draw_starting_hand('YOUR TURN')
while user_hand <21:
    prompt = input(f"You have {user_hand}. Hit (y/n)? " )
    if prompt == 'y':
        card_value=draw_card()
        user_hand += card_value
        if user_hand>21:
            break
    elif prompt == 'n':
        break
    else:
        print("Sorry I didn't get that.")
print_end_turn_status(user_hand)

# DEALER SECTION 
dealer_hand = draw_starting_hand('DEALER TURN')
while dealer_hand<17:
    print(f"Dealer has {dealer_hand}.")
    card_value = draw_card()
    dealer_hand += card_value
print_end_turn_status(dealer_hand)

#  END STATUS 
print_end_game_status(user_hand, dealer_hand)



