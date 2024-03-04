# Monte Carlo
def montecarlo(n):
  import random
  import math
  k=0
  for i in range(n):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    # print(x,y)
    if x**2+y**2<=1:
      k+=1
  return 4*k/n
montecarlo(5)
print(montecarlo(5))
print(montecarlo(50))
print(montecarlo(500))
