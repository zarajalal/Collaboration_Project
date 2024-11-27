
import random

def BotRoll(three_dice, duplicate_dice):
    '''
    Determines whether the bot will reroll the current dice or score the dice
    '''
    score = 0
    sum_of_doubled = 0
    
    for index in duplicate_dice:
        if index == -1:
            sum_of_doubled += three_dice[index]
    if sum_of_doubled == 0:
        # no double
        if three_dice[0] + three_dice[1] + three_dice[2] ==  :
            # if the dice rolls without a duplicate number is a "good sum" then lean towards keeping the dice
            score += 1

    else:
        # there is a double
        if sum_of_doubled >= 8:
        # min is 1 max is 6, middle is 3 or 4
        # higher than 6 means there is a good chance of a good roll
            # higher chance to keep a higher roll
            rand_choice_list = (2*three_dice[duplicate_dice.index(1)] - 2) * str(1) + (6 - three_dice[duplicate_dice.index(1)]) * str(0)
            if int(random.choice(rand_choice_list)) == 0:
                score -= 2
            else:
                score += 2
        else:
            rand_choice_list = (2*three_dice[duplicate_dice.index(1)]) * str(1) + (6 - three_dice[duplicate_dice.index(1)]) * str(0)
            score += int(random.choice(rand_choice_list))
        # [three_dice[duplicate_dice.index(1)]] * three_dice[duplicate_dice.index(1)] + [0] * (6 - three_dice[duplicate_dice.index(1)])
    if score >= 0:
        return "done"
    else:
        return ""
    
    # return "done" if random.choice(rand_choice_list) == 1 else ""

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
score_to_win = 100

# determines if the 2nd player is a computer
if "Computer" in players:
    play2Bot = True
else:
    play2Bot = False



# printing some title text
print(f"""
This is a \"Tuple Out\" Dice Game!
2 Players will take turns rolling 3 dice.
If 2 dice land on the same number, they will not be rerollable,
If 3 dice land on the same number, all the points for that round will be lost.
The player that reaches {score_to_win} first wins!
Good luck!
""")

while True:
    # Player wins if it is turn is player 1's and either player reaches over the score to win
    if players[list(players.keys())[0]] >= score_to_win and turn == 1:
        break
    elif players[list(players.keys())[1]] >= score_to_win and turn == 1:
        break

    # roll three random 6 sided dice
    three_dice = random.choices(range(1,7), k = 3)
    # Check if there are any values in a list that are duplicates and returns a list where the duplicated values are -1 in that position
    # Only can input a list of length 3
    duplicate_dice = [1,1,1]
    for i in range(len(three_dice)):
        for j in range(len(three_dice)):
            if not i == j:
                if three_dice[i] == three_dice[j]:
                    duplicate_dice[i] = -1
                    duplicate_dice[j] = -1

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
        if not duplicate_dice.count(-1) == 3:
            if turn == -1 and play2Bot:
                fin_roll = BotRoll(three_dice, duplicate_dice)
                None
            else:
                fin_roll = input("Only type \"done\" if happy with rolls\n")
            if fin_roll == "done":
                break
        else:
            if turn == 1:
                print(f"{list(players.keys())[0]} has TUPLED OUT (rolling three of the same)\nYour scored 0 points this round")
            elif turn == -1:
                print(f"{"The Computer" if list(players.keys())[1] == "Computer" else list(players.keys())[1]} has TUPLED OUT (rolling three of the same)\nYour scored 0 points this round")
            break

        # reroll the dice that are not duplicate numbers by check_duplicate
        if duplicate_dice[0] == 1:
            three_dice[0] = random.choice(range(1,7))
        if duplicate_dice[1] == 1:
            three_dice[1] = random.choice(range(1,7))
        if duplicate_dice[2] == 1:
            three_dice[2] = random.choice(range(1,7))
        
    # add score, make sure tupled out does not get added score
    if turn == 1 and not duplicate_dice.count(-1) == 3:
        players[list(players.keys())[0]] += three_dice[0] + three_dice[1] + three_dice[2]
    elif turn == -1 and not duplicate_dice.count(-1) == 3:
        players[list(players.keys())[1]] += three_dice[0] + three_dice[1] + three_dice[2]
    
    # change turn
    turn *= -1

    print(f"\nCurrent Scores\nPlayer 1: {players[list(players.keys())[0]]}\nPlayer 2: {players[list(players.keys())[1]]}\n")

# print the winner
if players[list(players.keys())[0]] >= score_to_win and players[list(players.keys())[1]] >= score_to_win:
    if players[list(players.keys())[0]] >= players[list(players.keys())[1]]:
        print("PLAYER 1 WON")
    if players[list(players.keys())[1]] >= players[list(players.keys())[0]]:
        print("PLAYER 2 WON")
    else:
        print("Player's TIED")
elif players[list(players.keys())[0]] >= score_to_win:
    print("PLAYER 1 WON")
else:
    print("PLAYER 2 WON")
