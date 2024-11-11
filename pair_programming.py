
import random


three_dice = random.choices(range(6), k = 3)
fixed = [1,1,1]

player1_score = 0
player2_score = 0


for i in range(three_dice):
    for j in range(three_dice):
        if not i == j:
            if three_dice[i] == three_dice[j]:
                fixed[i] = -1
                fixed[j] = -1




