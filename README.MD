
# README for dice_game_pairProgram.py

This program is a 1 versus 1 game or 1 versus computer competing for the most points. Whoever makes their score counter past 100 points wins

## This Program
- Takes in user input to roll and reroll 3 dice
- The sum of the 3 dice will be added to the corresponding player's score counter
- Rolling three of a kind will 'tuple out' and cause that player to score no points that round
- Hosts a AI that can play as player 2. Be careful, it is somewhat difficult to win against. Do not underestimate it for your own dignity.
- Prints a line graph that allows you to see the point accumulation and see who is in the lead!

## To Play
- Players alturnate between rolling 3 dice
- If two dice roll the same number, those two cannot be rerolled
- If three dice roll the same number, that player will not be able to score points for that round
- When the player is happy with their rolls, they type 'done' and the sum of the dice will be added to their score counter
- Typing 'hist' graphs the current standings of the game
- Tiebreaker rules exist: If both players reach or get over 100 points, whoever has the greater score will be declared the winner.
- The AI will play by these rules as well

### Example Play
1) Player 1 rolls [2, 4, 2]
2) Dice number 1 and 3 will not be able to be rerolled
3) Player 1 is happy with their rolls and will not reroll
4) Player 1 scores 8 points that round
5) Player 2 rolls [1, 3, 4]
6) Player 2 rerolls the numbers
7) Player 2 gets rolls [1, 5, 5]
8) Player 2 cannot reroll dice number 2 and 3 because they are the same
9) Player 2 rerolls again to get [5, 5 ,5]
10) Player 2 will not score any points that round
11) The score at the end of the round is 8 - 0 and Player 1 is winning.
12) The turn rotates back to Player 1
13) Player 1 types 'hist' and is now able to see the point accumulation of the entire game
14) Player 1 closes the graph and game continues as normal

