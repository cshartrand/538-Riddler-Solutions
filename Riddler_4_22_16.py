# FiveThirtyEight Riddler 4/22/16
# The Misanthropic Neighbors Problem
# By Chris Shartrand

import numpy as np
import random as rand
percentage = np.zeros(4)
for i in range(1,5):
    N = 10**i
    houses = np.zeros(N)
    check = np.zeros(N)
    while not (all(x==1 for x in check)):
        home_pick = rand.randint(0,N-1) #randomly pick a home to try to move into

        if home_pick == 0 and all(x == 0 for x in houses[home_pick:home_pick+2]):
            houses[home_pick] = 1
            check[home_pick] = 1

        elif home_pick == N-1 and all(x==0 for x in houses[home_pick-1:home_pick+1]):
            houses[home_pick] = 1
            check[home_pick] = 1

        elif all(x==0 for x in houses[home_pick-1:home_pick+2]):
            houses[home_pick] = 1
            check[home_pick] = 1

        else:
            check[home_pick] = 1

    percentage[i-1] = np.mean(houses)

print percentage
