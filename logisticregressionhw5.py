import numpy as np 
import random

def point():
	return (random.uniform(-1,1))


N=100
runs=1000

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
		correctLabels.append( perceptron(line,newpoint)) 
		points.append(newpoint)