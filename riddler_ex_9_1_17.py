#Five Thirty Eight Riddler Express Solution 9/1/17
#by Chris Shartrand
import numpy as np
trials = 1000000
count_list = np.zeros(trials)
for i in range(0,trials):
    free_throw_count = 0
    streak = 0
    p = 0.7
    while streak < 17:
        make = np.random.binomial(1,p)
        free_throw_count += 1
        if make == 1:
            streak += 1
        else:
            streak = 0
    count_list[i] = free_throw_count
average = np.mean(count_list) #approximately 1420
print average
