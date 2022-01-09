# Import the needed module
import os

# Define the command to clear the screen.
clear_screen_command = "clear"

# Clear the screen
os.system(clear_screen_command)

# Loop until a valid number of players has been entered.
# Needs to be at least 2 players in a game.
while True:
    how_many_players_input = input("Please enter how many people are playing: ")
    if how_many_players_input.isdigit():
        how_many_players = int(how_many_players_input)
        if how_many_players > 1:
            break
        print ("Invalid number of players")
    else:
        print ("Invalid input")

# Loop until a valid dealer has been entered.
# The input needs to be in the range from 1 to the number of players.
while True:
    player_deal_input = input("Please enter the player who is dealing: ")
    if player_deal_input.isdigit():
        player_deal = int(player_deal_input)
        if 1 <= player_deal <= how_many_players:
            player_deal -= 1
            break
        print ("Invalid player number")
    else:
        print ("Invalid input")

# These variables keep track of the player's
# past scores and their current total score.
player_total = []
player_score_current = []

# Append 0 to the total score list and an empty
# list for for the player scores
for i in range(0,how_many_players):
    player_total.append(0)
    player_score_current.append([])

# This variable keeps track of the number of turns.
number_of_runs = 0

# This function handles changing the score.
def change_score():
    # Check to make sure the function is not being called on the first run.
    if number_of_runs == 0:
        print("The game hasn't even began.  You can't change the score.")
        return

    # Loop until a valid player number has been entered.
    # The range is from 1 to number of players.
    while True:
        change_score_player_input = input("Please input the player number to change their score: ")
        if change_score_player_input.isdigit():
            change_score_player = int(change_score_player_input)
            if 1 <= change_score_player <= how_many_players:
                break
            print("Invalid player number")
        else:
            print("Invalid input")

    # Print all of the selected player's scores with an index number attached.
    for print_score in range(number_of_runs):
        print("{}\t - {}".format(print_score,player_score_current[change_score_player-1][print_score]))

    # Loop until a valid index number has been entered.
    # The range is from 0 to the number of turns.
    while True:
        change_score_index_input = input("Please input the index number of the score to change: ")
        if change_score_index_input.isdigit():
            change_score_index = int(change_score_index_input)
            if 0 <= change_score_index <= number_of_runs:
                break
            print("Invalid number")
        else:
            print("Invalid input")

    # Loop until a valid score has been entered.
    # A valid score is divisible by 5.
    while True:
        new_score_input = input("Please enter the new score: ")
        if new_score_input.isdigit():
            new_score = int(new_score_input)
            if new_score % 5 == 0:
                player_score_current[change_score_player-1][change_score_index] = new_score
                player_total[change_score_player-1] = 0
                for update_score_total in range(number_of_runs):
                    player_total[change_score_player-1] += player_score_current[change_score_player-1][update_score_total]
                break
            print("Invalid number")
        else:
            print("Invalid input")

# This function is responsible for getting a player's score
# and calling the change score function if the input is correct.
# A valid score is divisible by 5.
def get_score(player_number):
    while True:
        value_inputed = input("Please enter player {} score: ".format(player_number))
        if value_inputed == "change":
            change_score()
        else:
            if value_inputed.isdigit():
                value = int(value_inputed)
                if value % 5 == 0:
                    return value
                print("Invalid number")
            else:
                print("Invalid input")

# The main game loop.
# Loop until a player is over 500 and is not tied with anyone.
while True:
    # Print information on how is dealing then move the dealer to the next person.
    print ("Player {} deals".format(player_deal+1))
    player_deal += 1
    if player_deal >= how_many_players:
        player_deal = 0

    # Get each player's score in turn.
    for i in range(0,how_many_players):
        player_score_current[i].append(get_score(i+1))

    # Clear the screen.
    os.system(clear_screen_command)

    # Print each of the player's turn scores.
    for x in range(0, number_of_runs+1):
        for i in range(0,how_many_players):
            print(player_score_current[i][x], end = "")
            print("\t", end = "")
        print("")

    # Print a dividing line between the turn scores and the final scores.
    print ("-"*8*how_many_players)

    # Add this rounds score to the players total score.
    for i in range(0,how_many_players):
        player_total[i] += player_score_current[i][number_of_runs]

    # Print the player's total score.
    for i in range(0,how_many_players):
        print(player_total[i], end = "")
        print("\t", end = "")
    print("")

    # Check to see if a player has one the game and is not tied with anyone else.
    check = False

    # Check each player if their score is greater than 500.
    # If it is, loop again through all of the players to make sure
    # No other player has a larger score or is tied.  If these
    # conditions are meet, print the win message and exit.
    for i in range(0,how_many_players):
        if not(check):
            if player_total[i] >= 500:
                check = True
                for j in range(0,how_many_players):
                    if player_total[i] <= player_total[j] and i != j:
                        check = False
                if check:
                    print("Player {} wins".format(i+1))
    if check:
        break

    # Increment the number of turns which has occurred.
    number_of_runs += 1
