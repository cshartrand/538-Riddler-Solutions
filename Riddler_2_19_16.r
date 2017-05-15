simulations = 10000
correct.seat = rep(0,simulations)

for(j in 1:simulations){
  seat.number = seq(1,100,by=1)
  board.order = sample(seat.number,replace=FALSE)
  plane.seat = rep(0,100)
  first.choice = sample(seat.number,1)
  plane.seat[1] = first.choice
  
  for(i in 2:100){
  
    if (is.element(board.order[i],plane.seat) == TRUE){
        seat.choice = sample(seat.number,1)
        while(is.element(seat.choice,plane.seat) == TRUE){
          seat.choice = sample(seat.number,1)
        }
        plane.seat[i] = seat.choice
    }
    else{
      plane.seat[i] = board.order[i]
    }
  }
  
  if(board.order[100] == plane.seat[100]){
    correct.seat[j] = 1
  }
}

mean(correct.seat)