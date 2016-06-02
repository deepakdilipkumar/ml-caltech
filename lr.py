import numpy as np 
import random

def point():
	return (random.uniform(-1,1))

def label(weights,input):
	return np.sign(weights.dot(input))

N=100
runs=1000
avgein=0.0
avgeout=0.0

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
	lrLabels=[]
	for j in range(N):
		newpoint=np.array(([1,point(),point()]))
		correctLabels.append( label(line,newpoint)) 
		points.append(newpoint)

	input = np.array(points)
	output = np.array(correctLabels)
	weights = np.dot(np.dot(np.linalg.inv(np.dot(input.T,input)),input.T),output)
	ein=0.0
	for j in range(N):
		if label(weights,points[j])!=correctLabels[j]:
			ein+=1

	ein/=N
	avgein+=ein

	eout=0.0
	for j in range(1000):
		randpoint=np.array(([1,point(),point()]))
		if label(weights,randpoint)!=label(line,randpoint):
			eout+=1

	eout/=1000
	avgeout+=eout
	print(i)

avgeout/=runs
avgein/=runs
print(avgein)
print(avgeout)