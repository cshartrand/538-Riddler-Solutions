# 6/2/2017 FiveThirtyEight Riddler Express
# NBA Finals Series Length Problem
import numpy as np
simulations = 50000
series_counts = np.zeros((simulations,3))
probs = [.5,.6,.7]

for i in range(0,len(probs)):
    p = probs[i]

    for j in range(0,simulations):
        won_series = np.zeros(2)
        total_games = 0

        while won_series[0] < 4 and won_series[1] < 4:
            win = np.random.binomial(1,p)

            if win == 1:
                won_series[0] = won_series[0] + 1
            else:
                won_series[1] = won_series[1] + 1


        total_games = np.sum(won_series)
        series_counts[j,i] = total_games

    print "Done with %s probability of winning series!" % p

print "The results, based on %s simulations!" % simulations
print np.mean(series_counts[:,0])
print np.mean(series_counts[:,1])
print np.mean(series_counts[:,2])
