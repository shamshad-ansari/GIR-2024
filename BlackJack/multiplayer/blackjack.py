# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.


def main():

  players = get_players()

  while players:
    play_round(players)
    dealer_hand = dealer_play()
    # players = remove_eliminated(players)

    # GAME RESULT
    print_header("GAME RESULT")
    for player in players:  
      player_score = print_end_game_status(player['name'], player["hand"], dealer_hand, player['score'])
      player['score'] = player_score
      if player['score'] == 0:
        print(player['name'] + ' eliminated!')
        players.remove(player)
      
    if not players:
      break

    another_hand = input("Do you want to play another hand (y/n)? ")
    if another_hand != 'y':
      break

# Player's Section
def get_players():
  num_players = int(input("Welcome to Blackjack! How many players? "))
  players = []
  for i in range(1, num_players+1):
    name = input(f"Enter player {i}'s name: ")
    players.append({"name": name, "score": 3, "hand": 0})
  return players

def play_round(players):
  for player in players:
    if player['score'] > 0:
      player_name = player["name"].upper() + "'S"
      player["hand"] = draw_starting_hand(player_name)
      should_hit = 'y'
      while player["hand"] < 21:
        should_hit = input("You have {}. Hit (y/n)? ".format(player["hand"]))
        if should_hit == 'n':
          break
        elif should_hit != 'y':
          print("Sorry I didn't get that.")
        else:
          player["hand"] += draw_card()
      print_end_turn_status(player["hand"])
      if player['score'] == 0:
        players.remove(player)
  
# Dealer's Section
def dealer_play():
  dealer_hand = draw_starting_hand("DEALER")
  while dealer_hand < 17:
    print("Dealer has {}.".format(dealer_hand))
    dealer_hand = dealer_hand + draw_card()
  print_end_turn_status(dealer_hand)
  return dealer_hand


main()
