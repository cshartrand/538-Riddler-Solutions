# Chris Shartrand
# FiveThirtyEight Riddler Express from 1/20/17
# The Lazy Day Coin Flip Problem

import numpy as np
sim_runs = 50000
win_count = 0

for i in np.arange(0,sim_runs):
    first = 0 #initialize first flippers number of heads
    second = 0 #initialize second flippers number of heads
    
    while first < 10 and second < 10:
        p = np.random.uniform(0,1,2) #initialize 2 RV's to represent the coin flips
        
        if p[0] > 0.5: #denotes heads for first flipper
            first = first +1
            if first > 9:
                win_count = win_count + 1 #keep track of number of times first flipper has won
        if p[1] > 0.5: #denotes heads for second flipper
            second = second + 1

(win_count*1.0)/sim_runs