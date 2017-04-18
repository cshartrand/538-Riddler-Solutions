# 4/14/17 FiveThirty Eight Riddler 
# The Supreme Court Conundrum
# Christopher Shartrand
##############################################################
years = 5000 #initialize what we define as a long term for the measure of vacancies
runs = 5000 #initialize how many simulations we will run
lr.vacant = numeric(runs) #to hold the long run vacancies for all of our simulations

for(k in 1:runs){

  #Run 'runs' many simulations
  justices = rep(0,9) #initialize an empty bench
  president = rbinom(1,1,.5) #initialize the president
  senate = rbinom(1,1,.5) #initialize the senate
  vacancies = rep(0,years)
  
  for (i in 1:years){
  
    #Run the election of the senate
    if (i %% 2 == 0){
      senate = rbinom(1,1,.5)
      senate
    }
  
    #Run the election for the president
    if(i %% 4 == 0){
      president = rbinom(1,1,.5)
      president
    }
  
    #Fill the Supreme Court or fail to fill Supreme Court
    for(j in 1:9){
      if(justices[j] <= 1 && president == senate){
        justices[j] = runif(1,0,40)
      }else if(justices[j] <= 1 && president != senate){
        justices[j] = 0
      } #else{
        #break
      #}
    }
  
    #Calculate the empty seats
    for(j in 1:9){
      if(justices[j] == 0){
        vacancies[i] = vacancies[i] + 1
      }
    }
    
    justices = justices - 1
  }

  lr.vacant[k] = vacancies[years]  
}

expected.lr = mean(lr.vacant)