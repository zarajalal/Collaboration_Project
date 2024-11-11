
import random

def check_duplicate(lis:list):
    '''Method to check if there are any values in a list that are duplicates and returns a list where the duplicated values are -1 in that position
    Only can input a list of length 3
    '''
    dup = [1,1,1]
    for i in range(len(lis)):
        for j in range(len(lis)):
            if not i == j:
                if lis[i] == lis[j]:
                    dup[i] = -1
                    dup[j] = -1
    return dup

# initialize variables
three_dice = [0,0,0]

player1_score = 0
player2_score = 0

# turn is set to player 1, -1 is player 2's turn
turn = 1

# score to reach
max_score = 100

while not player1_score >= max_score or player2_score >= max_score:
    # roll three random 6 sided dice
    three_dice = random.choices(range(1,7), k = 3)

    # code for the player turn
    fin_roll = ""
    while not fin_roll == "done":
        print("Current rolls: ", three_dice)
        print(f"It is currently",end=" ")
        # print who's turn it is
        if turn == 1:
            print("Player 1's turn")
        elif turn == -1:
            print("Player 2's turn")

        # check if the roll is tupled out (all three dice are the same number) or reroll dice
        if not check_duplicate(three_dice).count(-1) == 3:
            fin_roll = input("Only type \"done\" if happy with rolls\n")
        else:
            print("You have TUPLED OUT (rolling three of the same)\nYour scored 0 points this round")
            fin_roll = 'done'

        # reroll the dice that are not duplicate numbers by check_duplicate
        if check_duplicate(three_dice)[0] == 1:
            three_dice[0] = random.choice(range(1,7))
        if check_duplicate(three_dice)[1] == 1:
            three_dice[1] = random.choice(range(1,7))
        if check_duplicate(three_dice)[2] == 1:
            three_dice[2] = random.choice(range(1,7))
        
    # add score, make sure tupled out does not get added score
    if turn == 1 and not check_duplicate(three_dice).count(-1) == 3:
        player1_score += three_dice[0] + three_dice[1] + three_dice[2]
    elif turn == -1 and not check_duplicate(three_dice).count(-1) == 3:
        player2_score += three_dice[0] + three_dice[1] + three_dice[2]
    
    # change turn
    turn *= -1

    print(f"\nCurrent Scores\nPlayer 1: {player1_score}\nPlayer 2: {player2_score}\n")

# print the winner
if player1_score >= 20:
    print("PLAYER 1 WON")
elif player2_score >= 20:
    print("PLAYER 2 WON")
