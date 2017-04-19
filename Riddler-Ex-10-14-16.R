##Riddler Express 10/14/16
##by Chris Shartrand Ballston Lake, NY
x = matrix(,100,2) # initialize matrix
for(i in 1:100){
  x[i,1] = i
} # first column numbers the coins 1 to 100
for(i in 1:100){
  x[i,2] = 1
}##second column initializes the coins into a face up scenario 
##let us call heads == 1 and tails == 0
is.wholenumber <-
  function(x, tol = .Machine$double.eps^0.5)  abs(x - round(x)) < tol
##function to check if 1,2,3,...100 is a multiple of the coin number
##start the flipping process
for(i in 1:100){
  for(j in 1:100){
  if(is.wholenumber(x[j,1]/i)==1){
    if(x[j,2]==1){
      x[j,2]=0
    }
      else{
        x[j,2]=1
      }
  }
}
}
x #output the solution
# the squares are face down, as in x[i,2]==0
