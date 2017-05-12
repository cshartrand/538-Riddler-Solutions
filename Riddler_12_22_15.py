#FiveThirtyEight Riddler 12-22-15
#The Sibling Cellphone Distraction Problem
#by Chris Shartrand
import numpy as np
from random import randint

simulations = 10000
expected_time = np.zeros(simulations)

for i in range(0,simulations):
    time = 0
    brother = randint(1,5)
    sister = randint(1,5)

    if brother == sister:
        time = brother
    else:
        while(brother and sister != 0):
            time = time + 1
            brother = brother - 1
            sister = sister - 1

            if brother == 0:
                brother = randint(1,5)
            elif sister == 0:
                sister = randint(1,5)

    expected_time[i] = time

print np.mean(expected_time)
