import numpy as np 
import random
from sklearn import svm

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
avgplaAccuracy=0.0
avgsvmAccurary=0.0

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
	plaLabels=[]
	plaweights=np.array([0,0,0])
	for j in range(N):
		newpoint=np.array(([point(),point()]))
		correctLabels.append( perceptron(line,np.hstack((1,newpoint)))) 
		plaLabels.append(perceptron(plaweights,np.hstack((1,newpoint))))
		points.append(newpoint)
	numIterations=0

	print(correctLabels)
	while (correctLabels!=plaLabels):
		incorrect=mismatch(correctLabels,plaLabels)
		learningIndex=random.choice(incorrect)
		plaweights=learning(plaweights,np.hstack((1,points[learningIndex])),correctLabels[learningIndex])
		for j in range(N):
			plaLabels[j]=perceptron(plaweights,np.hstack((1,points[j])))
		numIterations+=1

	plaaccuracy=0.0
	testpoints=[]
	for j in range(1000):
		testPoint=np.array(([1,point(),point()]))
		testpoints.append(testPoint[1:])
		if(perceptron(plaweights,testPoint)==perceptron(line,testPoint)):
			plaaccuracy+=1

	plaaccuracy/=1000
	avgplaAccuracy+=plaaccuracy
	clf=svm.SVC()
	clf.fit(points,correctLabels)
	svmprediction=clf.predict(testpoints)
	svmaccuracy=0.0
	for j in range(1000):
		if(svmprediction[j]==perceptron(line,np.hstack((1,testpoints[j])))):
			svmaccuracy+=1

	svmaccuracy/=1000
	avgsvmAccurary+=svmaccuracy
	print(i)


avgplaAccuracy/=runs
avgsvmAccurary/=runs
print(1-avgplaAccuracy)
print(1-avgsvmAccuracy)



