# 3-31-17 FiveThirtyEight Riddler Express
# Chris Shartrand
# Simulation of friends meeting for lunch. Assuming uniform distribution
# of arrival time.

import numpy as np
sims = 100000
friend1 = np.random.uniform(0,60,sims)
friend2 = np.random.uniform(0,60,sims)
success = np.zeros(sims)
for i in range(0,sims):
    if friend1[i] > friend2[i]:
        time_diff = friend1[i] - friend2[i]
    elif friend2[i] > friend1[i]:
        time_diff = friend2[i] - friend1[i]
    else:
        time_diff = 0

    if time_diff <= 15:
        success[i] = 1
    else:
        success[i] = 0
np.mean(success)
