import random as rnd 

avg=0

for i in range(10000):
	e1 = rnd.uniform(0,1)
	e2 = rnd.uniform(0,1)
	avg+=min(e1,e2)

avg/=10000
print(avg)