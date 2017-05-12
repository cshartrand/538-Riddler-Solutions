# FiveThirtyEight Riddler 4/28/17
# The Colored Ball Problem
# by Chris Shartrand

import numpy as np
from random import randint
simulations = 50000
expected_runs = np.zeros(simulations)

for i in range(0,simulations):
    balls = [1,2,3,4]
    runs = 0

    while not (all(x==balls[0] for x in balls)):
        pulled1 = randint(0,3)
        pulled2 = randint(0,3)

        if pulled1 == pulled2:
            while(pulled1 == pulled2):
                pulled2 = randint(0,3)

        balls[pulled2] = balls[pulled1]
        runs = runs + 1

    expected_runs[i] = runs
print np.mean(expected_runs)
