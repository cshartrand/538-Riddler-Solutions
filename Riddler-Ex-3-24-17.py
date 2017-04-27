# Chris Shartrand
# FiveThirtyEight Riddler from 3/24/17
# The Baby Walk Problem

import numpy as np

sim_steps = 5000.
sim_runs = 1000
baby_location = np.zeros(sim_steps) #keep track of where baby is. Zero corresponds to clutching the couch. > 0 corresponds to number of steps away from couch
clutch = np.zeros(sim_runs) #Hold the clutch percentage for the number of simulation runs

for j in np.arange(0,sim_runs):
    for i in np.arange(0,sim_steps-1):
        if baby_location[i] > 0:
            p = np.random.uniform(0,1) #initialize a uniform RV to keep track of percent chance of movement
            if p < 0.25:
                baby_location[i+1] = baby_location[i] + 1 #denotes moving away from couch
            elif p >= 0.50:
                baby_location[i+1] = baby_location[i] - 1 #denotes moving back toward couch
            else:
                baby_location[i+1] = baby_location[i] #denotes remaining in place
        else:
            p = np.random.uniform(0,1) #initialize RV
            if p < 0.25:
                baby_location[i+1] = baby_location[i] +1 #denotes moving away from couch
            else:
                baby_location[i+1] = baby_location[i] #denotes clutching the couch
    
    clutch[j] = 1 - (np.count_nonzero(baby_location)/sim_steps)

np.mean(clutch)