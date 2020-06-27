#!/usr/bin/python
##If you  have a random generator function, which generates random floating value from
#0,1 or between 0,1
##use this function to estimate the value of pi
##

import random
def estimate_pi (n):
    num_points_circle=0
    num_points_total=0
    for i in range (n):
      x=random.uniform(0,1)
      y=random.uniform(0,1)
      d = x*x+y*y
      if ((d < 1)):
        num_points_circle+=1
      num_points_total+=1
    ratio = (num_points_circle/num_points_total)
    estimated_pi = 4*ratio
    return estimated_pi 
ans=estimate_pi(100)
print(ans)

