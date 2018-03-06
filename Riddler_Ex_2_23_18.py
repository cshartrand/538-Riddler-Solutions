# FiveThirtyEight Riddler 1/5/18
# The Token Chance Problem
# by Chris Shartrand
import numpy as np


simulations = 1000000
me_winner = np.zeros(simulations)
p = 2./3

for sim in range(0,simulations):
    me_token = 1
    you_token = 2
    while me_token > 0 and you_token > 0:
        win = np.random.binomial(1,p)
        if win == 1:
            me_token += 1
            you_token -= 1
        else:
            me_token -= 1
            you_token += 1
    if me_token != 0:
        me_winner[sim] = 1

print 'My chance of winning is: ', np.mean(me_winner) # ~57%
