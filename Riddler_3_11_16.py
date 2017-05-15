# FiveThirtyEight Riddler
# The Underhand Freethrow Problem with Extension
# By Chris Shartrand

import numpy as np

#Initial Set-Up to find the variance
'''
simulations = 100000
ft_makes = np.zeros(simulations)
vals = 300
var_vals = np.zeros(vals)
percentage = np.zeros(vals)

for i in range(0,vals):
    var_vals[i] = 1 - .0025*i
    sd = np.sqrt(var_vals[i])

    for j in range(0,simulations):

        xy = np.random.normal(0,sd,2)
        if xy[0]**2 + xy[1]**2 < 1:
            ft_makes[j] = 1

    percentage[i] = np.mean(ft_makes)

for i, item in enumerate(percentage):
    print (i,item)
#variance ~= 0.355
'''

#Use the necessary variance to calulate the granny-shot percentage
'''
simulations = 100000
var = 0.355 #variance here is approximate due to the simulation results
# but thats quite okay
sd = np.sqrt(var)
percentage = 0
ft_makes = np.zeros(simulations)

for i in range(0,simulations):
    #Exclude x because there is no lateral movement anymore
    y = np.random.normal(0,sd,1)
    if abs(y) < 1:
        ft_makes[i] = 1

percentage = np.mean(ft_makes)
print percentage #makes roughly 90.5 percent of the freethrow shots
'''

#Finally let's add a cool extension
#In the english measurement system, the diameter of a hoop is 18 inches,while the diameter of the basketball is 9.55 inches.
#This leaves 4.225 inches of space on the sides of the ball if it goes into the hoop directly center.
#Assume we continue to shoot underhand such that there is no lateral movement of the ball.
#Now however we must make sure there is enough room for the ball to enter the hoop otherwise it will hit the rim and fly out
#Hence we no longer have a radius of 1 for our Y location of the shot. Instead we must have 4.775in/9in = 0.531 ratio of room
#to make the shot. What is our freethrow percentage now with the current variance?
simulations = 100000
var = 0.355
sd = np.sqrt(var)
ft_makes = np.zeros(simulations)
percentage = 0

for i in range(0,simulations):
    y = np.random.normal(0,sd,1)
    if abs(y) < .531:
        ft_makes[i] = 1

percentage = np.mean(ft_makes)
print percentage #approximately 62% freethrow shooter now
