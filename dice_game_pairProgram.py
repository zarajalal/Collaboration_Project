
import random

# def BotRoll(three_dice):
#     '''
#     Determines whether the bot will reroll the current dice or score the dice
#     '''
#     score = 0
#     val_of_doubled = 0
#     for index in check_duplicate(three_dice):
#         if index == -1:
#             val_of_doubled += three_dice[index]
#     if val_of_doubled == 0:
#         # no double
#         if three_dice[0] + three_dice[1] + three_dice[2] ==  :

#     elif val_of_doubled >  :
#         score += 1
#     else:
#         # valofdoubled is less than value (low double)
#         score -= 1

    

#     if score <= 0:
#         return "done"
#     else:
#         return ""

# conditions that make a good roll
# total is fairly high: 556, 456
# relatively value reroll 112 -> 116
# roll has room to be better 123 -> 334
# 

# '''
# 112
# 4

# 334
# 10
# 443
# 11

# 566
# 17
# '''

# '''
# 123
# 124
# 125
# 126
# 134
# 135
# 136
# 145
# 146
# 156

# 234
# 235
# 236
# 245
# 246
# 256

# 345
# 346
# 356

# 456
# '''


# initialize variables
three_dice = [0,0,0]


name1 = input("Name of Player 1 or PRESS ENTER for default name\n")
name2 = input("Name of Player 2 or PRESS ENTER for default name\nType BOT to play against Player 2 as Computer\n")
players = {
    "Player 1" if name1 == "" else name1: 0,
    "Computer" if name2 == "BOT" else ("Player 2" if name1 == "" else name1): 0,
}

# turn is set to player 1, -1 is player 2's turn
turn = 1

# score to reach
max_score = 100

# determines if the 2nd player is a computer
if "Computer" in players:
    play2Bot = False
else:
    play2Bot = True



# printing some title text
print(f"""
This is a \"Tuple Out\" Dice Game!
2 Players will take turns rolling 3 dice.
If 2 dice land on the same number, they will not be rerollable,
If 3 dice land on the same number, all the points for that round will be lost.
The player that reaches {max_score} first wins!
Good luck!
""")


while True:
    if players[list(players.keys())[0]] >= max_score and turn == 1:
        break
    elif players[list(players.keys())[1]] >= max_score and turn == 1:
        break
    print(players)
    if input("" == "s"):
        break

    # roll three random 6 sided dice
    three_dice = random.choices(range(1,7), k = 3)
    # Check if there are any values in a list that are duplicates and returns a list where the duplicated values are -1 in that position
    # Only can input a list of length 3
    duplicate_Dice = [1,1,1]
    for i in range(len(three_dice)):
        for j in range(len(three_dice)):
            if not i == j:
                if three_dice[i] == three_dice[j]:
                    duplicate_Dice[i] = -1
                    duplicate_Dice[j] = -1


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
        if not duplicate_Dice.count(-1) == 3:
            if turn == -1 and play2Bot: 
                # fin_roll = BotRoll(three_dice)
                None
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
        if duplicate_Dice[0] == 1:
            three_dice[0] = random.choice(range(1,7))
        if duplicate_Dice[1] == 1:
            three_dice[1] = random.choice(range(1,7))
        if duplicate_Dice[2] == 1:
            three_dice[2] = random.choice(range(1,7))
        
    # add score, make sure tupled out does not get added score
    if turn == 1 and not duplicate_Dice.count(-1) == 3:
        player1_score += three_dice[0] + three_dice[1] + three_dice[2]
    elif turn == -1 and not duplicate_Dice.count(-1) == 3:
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
