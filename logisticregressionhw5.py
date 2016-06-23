import numpy as np 
import random
import math

def point():
	return (random.uniform(-1,1))

def einGrad(x,y,weights):
	return (y*x/(1+math.exp(y*weights.dot(x))))

def error(x,y,weights):
	return (math.log(1+math.exp(-y*weights.dot(x))))

N=100
runs=1000
learning=0.01
tolerance=0.01
numcheck=1000
avg

for i in range(runs):
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
	weight=np.array([0,0,0])
	oldweight=np.array([1,1,1])
	diff = weight-oldweight
	while(diff.dot(diff)>tolerance):
		eingradient=0
		for j in range(N):
			eingradient+=einGrad(newpoint(j),correctLabels(j),weights)

		eingradient/=N
		weights-=learning*eingradient


