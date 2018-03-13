# FiveThirtyEight Riddler 12/22/17
# The 6 Player Circle Problem
# by Chris Shartrand
import numpy as np
from random import sample
from itertools import cycle
# Create dictionary of where the money goes
d = { 0 : {0: 5,1: 'the_pot',2: 1},
    1 : {0: 0,1: 'the_pot',2: 2},
    2 : {0: 1,1: 'the_pot',2: 3},
    3 : {0: 2,1: 'the_pot',2: 4},
    4 : {0: 3,1: 'the_pot',2: 5},
    5 : {0: 4,1: 'the_pot',2: 0}
    }
simulations = 1000000
total_rounds = []
for i in range(0,simulations):
    player_money = [3]*6
    players = range(0,6)
    round_num = 0
    for j in cycle(players):
        # roll a die to figure out if money goes left, right or to the pot
        # if a player has no more money, they don't get a turn
        rolls = sample(range(1,7),min(player_money[j],3))
        for roll in rolls:
            if roll in [1,2]:
                money_move = d[j][0]
                player_money[j] -= 1
                player_money[money_move] +=1
            elif roll in [5,6]:
                money_move = d[j][2]
                player_money[j] -= 1
                player_money[money_move] +=1
            else:
                player_money[j] -= 1
        round_num += 1
        if player_money.count(0) >= len(player_money) - 1:
            break
    total_rounds.append(round_num)
print np.mean(total_rounds) # 24.879488 over 1 million simulations
