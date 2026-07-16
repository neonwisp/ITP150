"""
basketball_game.py
@Author: ITP 150 Ashlee Raya
Date Created: 7/14/2026
This program simulates a one-on-one basketball game using nested for loops,
if structures, and Python's random.randint() function to generate points. There
are 4 quarters in a basketball game, and each quarter has 12 minutes thus 720
seconds. In our basketball game, each player takes a shot every 30 seconds, and
we use the Python random function to choose if the player made one of the 
following shots in a 30 second interval. 
0 - Air Ball
1 - Free Throw
2 - Two Pointer
3 - Three Pointer
The score for each player is summed and an if statement is used to display the 
name of the winner after the game ends.
"""
 
 
import random
counter = 0
 
print('Play a One on One Basketball Game with your 2 favorite players!')
player1 = input('Please enter the name for Player1:\n')
player2 = input('Please enter the name for Player2:\n')
player1_score = 0
player2_score = 0
 

# for loop to count the quarters from 1 to 4
for quarter in range(1, 5):  # same as for i in range(1, 5, 1):
    print()
    print(('-' * 26), 'Quarter', quarter, ('-' * 26))
    print(f'{(' ' * 8)}{player1:<30s}{player2:<30s}')
    print(f'{"Shot #":8s}{"Shot":15s}{"Score":15s}{"Shot":15s}{"Score":15s}')

    # There are 12 minutes in each quarter and 60 seconds in a minute thus 720
    # seconds. We want each player to take a shot within a 30 second interval.
    for j in range(720, 0, -30):
        player1_shot = random.randint(0, 3)
        player2_shot = random.randint(0, 3)
        counter = counter + 1  # counter += 1
        # if statement assigns either 0, 1, 2, or 3 points for player 1
        if player1_shot == 0:
            player1_shotmade = "Air Ball"
        elif player1_shot == 1:
            player1_shotmade = "Free Throw"
        elif player1_shot == 2:
            player1_shotmade = "Two Pointer"
        else:
            player1_shotmade = "Three Pointer"

        # if statement assigns either 0, 1, 2, or 3 points for player 2
        if player2_shot == 0:
            player2_shotmade = "Air Ball"
        elif player2_shot == 1:           player2_shotmade = "Free Throw"
        elif player2_shot == 2:
           player2_shotmade = "Two Pointer"
        else:
           player2_shotmade = "Three Pointer"

        player1_score = player1_score + player1_shot
        player2_score = player2_score + player2_shot

        print(f'{counter:<8d}{player1_shotmade:<15s}{player1_score:<15d}\
{player2_shotmade:<15s}{player2_score:<15d}')

# if statement to determine the winner
if player1_score > player2_score:
    print(player1, " bringing a W!")
elif player2_score > player1_score:
    print(player2, " bringing a W!")
else:
    print("Tie Game...Go Home...See ya' later!")
