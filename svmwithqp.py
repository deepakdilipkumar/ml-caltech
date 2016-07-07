import numpy as np 
import random
from cvxopt import matrix,solvers

def perceptron(weights,input):
	return np.sign(weights.dot(input))

def svmpred(weights,b,input):
	return np.sign(weights.dot(input)+b)

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

def minimumindex(array):
	mini = 10000
	index = 0
	for i in range(len(array)):
		if(array[i]<mini):
			mini=array[i]
			index=i

	return(index)

N=10
runs=1000
avgplaAccuracy=0.0
avgsvmAccuracy=0.0
svmbetter=0.0

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
	plaweights=np.array([0,0,0])
	correctLabels=[1]
	while(len(np.unique(correctLabels))==1):
		points=[]
		correctLabels=[]
		plaLabels=[]
		for j in range(N):
			newpoint=np.array(([point(),point()]))
			correctLabels.append( perceptron(line,np.hstack((1,newpoint)))) 
			plaLabels.append(perceptron(plaweights,np.hstack((1,newpoint))))
			points.append(newpoint)
		#print(len(np.unique(correctLabels)))

	#print(correctLabels)
	while (correctLabels!=plaLabels):
		incorrect=mismatch(correctLabels,plaLabels)
		learningIndex=random.choice(incorrect)
		plaweights=learning(plaweights,np.hstack((1,points[learningIndex])),correctLabels[learningIndex])
		for j in range(N):
			plaLabels[j]=perceptron(plaweights,np.hstack((1,points[j])))
	
	#print(correctLabels)
	q = matrix(np.zeros(N)+1)
	G = matrix(-np.eye(N))
	h = matrix(np.zeros(N))
	A = matrix(correctLabels,(1,N))
	b = matrix(np.zeros(1))

	P = np.zeros((N,N))

	for j in range(N):
		for k in range(N):
			P[j,k]=correctLabels[j]*correctLabels[k]*points[j].dot(points[k])

	P = matrix(P)
	sol=solvers.qp(P, q, G, h, A, b)

	alpha=np.array(sol['x'])
	#print(alpha)

	svmweights=np.array(np.zeros(2))
	for j in range(N):
		svmweights+=correctLabels[j]*alpha[j]*points[j]

	#print(svmweights)
	svindex = minimumindex(alpha)
	b = (1/correctLabels[svindex])-svmweights.dot(points[svindex])
	#print(b)

	plaaccuracy=0.0
	svmaccuracy=0.0


	for j in range(1000):
		testpoint=np.array(([1,point(),point()]))
		correctlabel = perceptron(line,testpoint)
		if(perceptron(plaweights,testpoint)==correctlabel):
			plaaccuracy+=1

		if(svmpred(svmweights,b,testpoint[1:])==correctlabel):
			svmaccuracy+=1

	plaaccuracy/=1000
	avgplaAccuracy+=plaaccuracy
	svmaccuracy/=1000
	avgsvmAccuracy+=svmaccuracy
	if(svmaccuracy>plaaccuracy):
		svmbetter+=1
	print(i)

svmbetter/=runs
avgplaAccuracy/=runs
avgsvmAccuracy/=runs
print(1-avgplaAccuracy)
print(1-avgsvmAccuracy)
print(1-svmbetter)


