#FiveThirtyEight Riddler Express 5/19/2017
#by Chris Shartrand
#The Ticketed Carpool Problem

simulations = 1000000
trips.simulation = rep(0,simulations)
drivers = c(1,2,3,4)
ticket.probs = c(.1,.15,.2,.25)

for (i in 1:simulations){
tickets = rep(0,4)
trips = 0

  while (tickets[1] < 3 | tickets[2] < 3 | tickets[3] < 3 | tickets[4] < 3){
    driver = sample(drivers,1)

    while(tickets[driver]>=3){
      driver = sample(drivers,1)
    }
    pulled.over = rbinom(1,1,ticket.probs[driver])
  
    if (pulled.over == 1){
      tickets[driver] = tickets[driver] + 1
    }
  trips = trips + 1
  }
trips.simulation[i] = trips
}

days.lasted = mean(trips.simulation)/2
