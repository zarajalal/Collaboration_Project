
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

while not player1_score or player2_score >= 20:
    

    fin_roll = ""
    while not fin_roll.lower == "done":
        if check_duplicate(three_dice)[0] == 1:
            three_dice[0] = random.sample(range(1,7), k = 1)
        if check_duplicate(three_dice)[1] == 1:
            three_dice[1] = random.sample(range(1,7), k = 1)
        if check_duplicate(three_dice)[2] == 1:
            three_dice[2] = random.sample(range(1,7), k = 1)

        fin_roll = input("Type done if happy with rolls")
    
