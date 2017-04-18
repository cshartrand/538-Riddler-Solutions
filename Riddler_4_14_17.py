import numpy as np
years = 5000
runs = 5000
lr_vacant = np.zeros(runs)
for k in range(0,runs):
    #Initialize empty bench, what party has president, senate, and array to hold # of vacancies
    justices = np.zeros(9)
    president = np.random.binomial(1,.5)
    senate = np.random.binomial(1,.5)
    vacancies = np.zeros(years)

    for i in range(0,years):
        #Run election of the senate
        if i % 2 == 0:
            senate = np.random.binomial(1,.5)
        #Run election of the presidency
        if i % 4 == 0:
            president = np.random.binomial(1,.5)
        #Fill the Supreme Court or Fail to fill the Supreme Court
        for j in range(0,9):
            if justices[j] <= 1 and president == senate:
                justices[j] = np.random.uniform(0,40,1)
            elif justices[j] <= 1 and president != senate:
                justices[j] = 0
        #Calculate the number of empty seats
        for j in range(0,9):
            if justices[j] == 0:
                vacancies[i] = vacancies[i] + 1
        #Take a year away from death or retirement from bench
        justices = justices - 1

    lr_vacant[k] = vacancies[years-1]

#take mean of long run vacancies from multiple simulations
expected_lr = np.mean(lr_vacant)
print (expected_lr)
