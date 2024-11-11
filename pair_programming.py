
import random

def check_duplicate(lis:list):
    dup = [1,1,1]
    for i in range(len(lis)):
        for j in range(len(lis)):
            if not i == j:
                if lis[i] == lis[j]:
                    dup[i] = -1
                    dup[j] = -1
    return dup


three_dice = random.choices(range(1,7), k = 3)

player1_score = 0
player2_score = 0

turn = 1

while not player1_score >= 20 or player2_score >= 20:
    fin_roll = ""
    while not fin_roll.lower == "done":
        print("Current rolls: ", three_dice)
        if check_duplicate(three_dice)[0] == 1:
            three_dice[0] = random.sample(range(1,7), k = 1)
        if check_duplicate(three_dice)[1] == 1:
            three_dice[1] = random.sample(range(1,7), k = 1)
        if check_duplicate(three_dice)[2] == 1:
            three_dice[2] = random.sample(range(1,7), k = 1)

        if not check_duplicate(three_dice).count == 3:
            fin_roll = input("Type done if happy with rolls")
        else:
            print("You have ")
    if turn == 1:
        player1_score = three_dice[0] + three_dice[1] + three_dice[2]
        turn = 2
    elif turn == 2:
        player2_score = three_dice[0] + three_dice[1] + three_dice[2]
        turn = 1

    print(f"Current Scores\nPlayer 1: {player1_score}\nPlayer 2: {player2_score}\n")

if player1_score >= 20:
    print("PLAYER 1 WON")
elif player2_score >= 20:
    print("PLAYER 2 WON")
