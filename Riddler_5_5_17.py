# FiveThirtyEight Riddler 5-5-2017 Solution
# By Chris Shartrand
# The Lucky Derby Problem

import numpy as np
simulations = 10000
horse_wins = np.zeros(20)

for i in range(0,simulations):
    horse_location = np.zeros(20) #initialize the location of horse for each simulation
    winner = 0

    while (winner != 1): #will quit the while loop when a horse 'crosses the finish line'
        horse_probability = np.zeros(20) #initialize horse probability of forward/backward

        for j in range(0,20):
            horse_probability[j] = np.random.binomial(1,.5+.02*(j+1)) #creates proability of movement. 1 means forward, 0 means backward

        for k in range(0,20):
            if horse_probability[k] == 1: #move horse forward if == 1
                horse_location[k] = horse_location[k] + 1
            else: #move horse backward if == 0
                horse_location[k] = horse_location[k] - 1

        for l in range(0,20):
            if horse_location[l] == 200:
                horse_wins[l] = horse_wins[l] + 1
                winner = 1
            else:
                continue

horse_win_probs = horse_wins / simulations
print horse_win_probs
