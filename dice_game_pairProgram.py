
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

def BotRoll(dice):
    '''
    Determines whether the bot will reroll the current dice or score the dice
    '''
    check_duplicate(dice)
    return "done"

# initialize variables
three_dice = [0,0,0]

player1_score = 0
player2_score = 0

# turn is set to player 1, -1 is player 2's turn
turn = 1

# score to reach
max_score = 100

# determines if the 2nd player is a computer
play2Bot = False






# printing some title text
print(f"""
This is a \"Tuple Out\" Dice Game!
2 Players will take turns rolling 3 dice.
If 2 dice land on the same number, they will not be rerollable,
If 3 dice land on the same number, all the points for that round will be lost.
The player that reaches {max_score} first wins!
Good luck!
""")

#  
while not ((player1_score >= max_score and turn == 1) or player2_score >= max_score):
    # roll three random 6 sided dice
    three_dice = random.choices(range(1,7), k = 3)

    # code for the player turn
    fin_roll = ""
    while True:
        print("Current rolls: ", three_dice)
        print(f"It is currently",end=" ")
        # print who's turn it is
        if turn == 1:
            print("Player 1's turn")
        elif turn == -1:
            print("Player 2's turn")

        # check if the roll is tupled out (all three dice are the same number) or reroll dice
        if not check_duplicate(three_dice).count(-1) == 3:
            if turn == -1 and play2Bot: 
                fin_roll = BotRoll(three_dice)
            else:
                fin_roll = input("Only type \"done\" if happy with rolls\n")
            if fin_roll == "done":
                break
        else:
            if turn == 1:
                print("You have TUPLED OUT (rolling three of the same)\nYour scored 0 points this round")
            elif turn == -1 and play2Bot:
                print("Player 2 have TUPLED OUT (rolling three of the same)\nYour scored 0 points this round")
            break

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
if player1_score >= max_score and player2_score >= max_score:
    if player1_score >= player2_score:
        print("PLAYER 1 WON")
    if player2_score >= player1_score:
        print("PLAYER 2 WON")
    else:
        print("Player's TIED")
elif player1_score >= max_score:
    print("PLAYER 1 WON")
else:
    print("PLAYER 2 WON")
