# 538 Riddler Express 7-13-2018
# Soccer Penalty Kicks
# By Chris Shartrand
import numpy as np
past_five = []
simulations = 2500000

# Run 2.5 million simulations
for sim in range(0,simulations):
    winner = False
    kicks = np.random.binomial(1,.75,10) # Simulate the first 10 kicks to determine if sudden death occurs
    team_a = 0
    team_b = 0
    while not winner:
        team_a += sum(kicks[0:5])
        team_b += sum(kicks[5:])
        # If sum of binomial kicks equal, we will have sudden death round
        if team_a == team_b:
            past_five.append(1)
            winner = True
        else:
            past_five.append(0)
            winner = True
print sum(past_five)/float(simulations) # Comes out to approximately 29% of the time
