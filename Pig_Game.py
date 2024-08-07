# Objective: Be the first player to reach 50 points.

#Gameplay:
# On your turn, roll a die.
# If you roll a 2, 3, 4, 5, or 6:
# Add the roll to your turn total.
# Choose to roll again or hold.
# If you hold, add your turn total to your overall score.
# If you roll a 1:
# Your turn ends, and your turn total resets to zero.
# Winning: The first player to reach 50 points wins the game.


import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx],'\n')
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                curent_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                
            print("Your current score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)