
import random
import os

def BotRoll(three_dice, duplicate_dice):
    '''
    Determines whether the bot will reroll the current dice or score the dice
    scoring is in incomplete status, temporary code to decide keeping dice with random
    '''
    score = 0
    sum_of_doubled = 0
    
    for index in duplicate_dice:
        if index == -1:
            sum_of_doubled += three_dice[index]
    if sum_of_doubled == 0:
        # no double
        # if the dice rolls without a duplicate number is a "good sum" then lean towards keeping the dice
        rand_choice_list = (three_dice[0] * str(three_dice[0]) + (6 - three_dice[0]) * str(0) +
                            three_dice[1] * str(three_dice[1]) + (6 - three_dice[1]) * str(0) +
                            three_dice[2] * str(three_dice[2]) + (6 - three_dice[2]) * str(0)
                            )
        if int(random.choice(rand_choice_list)) == 0:
            score -= 2
        else:
            score += 2
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
    
    
# initialize variables
three_dice = [0,0,0]

# initialize a tuple of possible dice numbers
dice_face = (1,2,3,4,5,6)

# intialize a dictionary with the names of the two players or a player with a computer
name1 = input("Name of Player 1 or PRESS ENTER for default name\n")
name2 = input("Name of Player 2 or PRESS ENTER for default name\nType BOT to play against Player 2 as Computer\n")
players = {
    "Player 1" if name1 == "" else name1: 0,
    "Computer" if name2 == "BOT" else ("Player 2" if name1 == "" else name1): 0,
}

# turn is set to player 1, -1 is player 2's turn
turn = 1

# score to surpass/reach to win
score_to_win = 100

# determines if the 2nd player is a computer
if "Computer" in players:
    play2Bot = True
else:
    play2Bot = False

# keep track of who is in the lead
history = []

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
    # code for player's turn
    # Player wins if it is turn is player 1's and either player reaches over the score to win
    if players[list(players.keys())[0]] >= score_to_win and turn == 1:
        break
    elif players[list(players.keys())[1]] >= score_to_win and turn == 1:
        break

    # roll three random 6 sided dice
    three_dice = random.choices(dice_face, k = 3)
    # Check if there are any values in a list that are duplicates and returns a list where the duplicated values are -1 in that position
    # Only can input a list of length 3
    
    # code for the player dice rolls
    fin_roll = ""
    while True:
        # ensure the duplicated dice persist and mark them
        duplicate_dice = [1,1,1]
        for i in range(len(three_dice)):
            for j in range(len(three_dice)):
                if not i == j:
                    if three_dice[i] == three_dice[j]:
                        duplicate_dice[i] = -1
                        duplicate_dice[j] = -1
        
        print("Current rolls: ", three_dice)
        print(f"It is currently",end=" ")
        # print who's turn it is
        if turn == 1:
            print(f"{list(players.keys())[0]}'s turn")
        elif turn == -1:
            print(f"{list(players.keys())[1]}'s turn")

        # check if the roll is tupled out (all three dice are the same number) or reroll dice
        if not duplicate_dice.count(-1) == 3:
            if turn == -1 and play2Bot:
                # have the bot decide whether to reroll or not
                fin_roll = BotRoll(three_dice, duplicate_dice)
            else:
                # player decides to reroll or not
                fin_roll = input("Only type \"done\" if happy with rolls\nType \"hist\" to print a graphical representation of history\n")
            # add checks if the player may have typed done wrong
            if fin_roll == "done" or fin_roll == "one" or fin_roll == "dne" or fin_roll == "don" or fin_roll == "doe" or fin_roll == "oen" or fin_roll == "odne":
                # * Does this count as avoiding an error based on user input (PATT 5.2)
                # * I'm avoiding possible spelling errors the user might make if they intend to complete their roll
                break
            elif fin_roll == 'hist':
                # graph the point gain for both players over each turn
                None


                
        else:
            # print tupled out text
            if turn == 1:
                print(f"{list(players.keys())[0]} has TUPLED OUT (rolling three of the same)\nYour scored 0 points this round")
            elif turn == -1:
                print(f"{"The Computer" if list(players.keys())[1] == "Computer" else list(players.keys())[1]} has TUPLED OUT (rolling three of the same)\nYour scored 0 points this round")
            # turn ends
            break

        # reroll the dice that are not duplicate numbers
        if duplicate_dice[0] == 1:
            three_dice[0] = random.choice(dice_face)
        if duplicate_dice[1] == 1:
            three_dice[1] = random.choice(dice_face)
        if duplicate_dice[2] == 1:
            three_dice[2] = random.choice(dice_face)
        
    # add score, make sure tupled out does not get added score
    if turn == 1 and not duplicate_dice.count(-1) == 3:
        players[list(players.keys())[0]] += three_dice[0] + three_dice[1] + three_dice[2]
    elif turn == -1 and not duplicate_dice.count(-1) == 3:
        players[list(players.keys())[1]] += three_dice[0] + three_dice[1] + three_dice[2]
    
    # change turn
    turn *= -1

    # print the scores
    print(f"\nCurrent Scores\nPlayer 1: {players[list(players.keys())[0]]}\nPlayer 2: {players[list(players.keys())[1]]}",end="\n\n")

    # add history to who is in the lead
    if players[list(players.keys())[0]] > players[list(players.keys())[1]]:
        history.append("1")
    elif players[list(players.keys())[1]] > players[list(players.keys())[0]]:
        history.append("2")
    else:
        history.append("Tie")
# print the winner
if players[list(players.keys())[0]] >= score_to_win and players[list(players.keys())[1]] >= score_to_win:
    if players[list(players.keys())[0]] >= players[list(players.keys())[1]]:
        print(f"{str(list(players.keys())[0]).upper()} WON")
        history.append("Player 1 won")
    if players[list(players.keys())[1]] >= players[list(players.keys())[0]]:
        print(f"{str(list(players.keys())[1]).upper()} WON")
        history.append("Player 2 won")
    else:
        print("IT'S A TIED GAME")
        history.append("Tied")
elif players[list(players.keys())[0]] >= score_to_win:
    print(f"{str(list(players.keys())[0]).upper()} WON")
    history.append("Player 1 won")
else:
    print(f"{str(list(players.keys())[1]).upper()} WON")
    history.append("Player 2 won")

# save the history to a txt file for later use
with open(f"{os.getcwd()}\\game_history.csv", "a") as savefile:
    savefile.write(f"{history}",end="\n\n\n")