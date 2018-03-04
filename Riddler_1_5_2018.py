# FiveThirtyEight Riddler 1/5/18
# The Dwarf Bed Problem
# by Chris Shartrand

import numpy as np
import random
from random import randint

simulations = 1000000
dwarves = range(0,7)
beds = range(0,7)
old_dwarf = np.zeros(simulations)
incorrect_beds = np.zeros(simulations)

for i in range(0,simulations):
    beds = [True]*7 # set all of the beds to being "open" (true)
    incorrect = 0 # count the number of incorrect dwarf to beds we have on a given night
    for dwarf in dwarves:
        if dwarf == 0: # the jolly young dwarf chooses his own bed first
            bed_choice = randint(0,6)
            beds[bed_choice] = False # update to show it is an occupied bed
            if bed_choice != 0:
                incorrect += 1
        else:
            if beds[dwarf] == True: # check to see if a dwarf's own bed is open to sleep in
                beds[dwarf] = False
                if dwarf == 6: # if it is the oldest dwarf, count to show they slept in their own bed
                    old_dwarf[i] = 1
            else:
                open_beds = [idx for idx, x in enumerate(beds) if x] # get index of beds that are still open
                bed_choice = random.choice(open_beds)
                beds[bed_choice] = False
                incorrect += 1 # increment the fact that we do not have a correct dwarf to bed
    incorrect_beds[i] = incorrect



print "Probability old dwarf sleeps in their bed: ", np.mean(old_dwarf)
print "Expected number of dwarves who do not sleep in their own bed: ", np.mean(incorrect_beds)
