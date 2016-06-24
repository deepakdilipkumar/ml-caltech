import numpy as np 
import random
import math

def point():
	return (random.uniform(-1,1))

def einGrad(x,y,weights):
	return (-y*x/(1+math.exp(y*weights.dot(x))))

def error(x,y,weights):
	return (math.log(1+math.exp(-y*weights.dot(x))))

N=100
tests=100
learning=0.01
tolerance=0.01
numcheck=1000
avgeout=0.0
avgruns=0.0

for i in range(tests):
	p1 = np.array([point(),point()])
	p2 = np.array([point(),point()])
	x1=p1[0]
	y1=p1[1]
	x2=p2[0]
	y2=p2[1]	
	slope= (y2-y1)/(x2-x1)
	intercept= (y1*x2-y2*x1)/(x2-x1)
	line=np.array([-intercept,-slope,1])   # We want the sign of y-mx-c
	points=[]
	correctLabels=[]
	for j in range(N):
		newpoint=np.array(([1,point(),point()]))
		correctLabels.append( np.sign(line.dot(newpoint))) 
		points.append(newpoint)

	weights=np.array([0,0,0])
	oldweights=np.array([1,1,1])
	diff = weights-oldweights
	runs=0.0
	while(math.sqrt(diff.dot(diff))>tolerance):
		#eingradient=0.0
		oldweights=weights
		order=range(N)
		random.shuffle(order)
		for j in order:
			eingradient=einGrad(points[j],correctLabels[j],weights)
			weights=weights-learning*eingradient
		#eingradient/=N
		runs+=1.0
		diff=weights-oldweights
		#print(diff)

	#print(diff)
	avgruns+=runs
	eout=0.0
	for j in range(numcheck):
		newpoint=np.array([1,point(),point()])
		label=np.sign(line.dot(newpoint)) 
		eout+=error(newpoint,label,weights)

	eout/=numcheck
	avgeout+=eout
	print(i)

avgeout/=tests
avgruns/=tests
print(avgruns)
print(avgeout)
print(line)
print(weights)