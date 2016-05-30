import numpy as np 
import random

def perceptron(weights,input):
	return np.sign(weights.dot(input))

def learning(weights,input,label):
	return (weights+input*label)

def point():
	return (random.uniform(-1,1))

def mismatch(list1,list2):
	incorrect=[]
	for i in range(len(list1)):
		if (list1[i]!=list2[i]):
			incorrect.append(i)

	return incorrect


N=10
runs=1000
avgIterations=0

for i in range(runs):
	p1 = np.array([point(),point()])
	p2 = np.array([point(),point()])
	x1=p1[0]
	y1=p1[1]
	x2=p2[0]
	y2=p2[1]	
	slope= (y2-y1)/(x2-x1)
	intercept= (y1*x2-y2*x1)/(x2-x1)
	line=np.array([-intercept,-slope,1])
	points=[]
	correctLabels=[]
	plaLabels=[]
	weights=np.array([0,0,0])
	for j in range(N):
		newpoint=np.array(([1,point(),point()]))
		correctLabels.append( perceptron(line,newpoint)) #np.sign(newpoint[2]-slope*newpoint[1]-intercept))
		plaLabels.append(perceptron(weights,newpoint))
		points.append(newpoint)

	numIterations=0
	while (correctLabels!=plaLabels):
		incorrect=mismatch(correctLabels,plaLabels)
		learningIndex=random.choice(incorrect)
		weights=learning(weights,points[learningIndex],correctLabels[learningIndex])
		for j in range(N):
			plaLabels[j]=perceptron(weights,points[j])
		numIterations+=1

	avgIterations+=numIterations


avgIterations/=1000
print(correctLabels)
print(plaLabels)
print(avgIterations)




