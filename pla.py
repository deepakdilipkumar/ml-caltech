import numpy as np 
import random

def perceptron(weights,input):
	return np.sign(weights.dot(input))

def learning(weights,input,label):
	return (weights+input*label)

def point():
	return (random.uniform(-1,1))

N=10
runs=1000

for i in range(runs):
	p1 = np.array([point(),point()])
	p2 = np.array([point(),point()])
	slope=
	intercept=
	points=[]
	labels=[]
	for j in range(N):
		newpoint=np.array(([point(),point()]))
		labels.append(np.sign(newpoint[1]-slope*newpoint[0]-intercept))
		points.append(newpoint)
	