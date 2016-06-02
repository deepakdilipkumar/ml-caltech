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

	points=[]
	transformedpoints=[]
	correctLabels=[]
	lrLabels=[]
	for j in range(N):
		newpoint=np.array(([1,point(),point()]))
		x=newpoint[1]
		y=newpoint[2]
		transformedpoint=[1,x,y,x*y,x*x,y*y]
		correctLabels.append( np.sign(pow(x,2)+pow(y,2)-0.6)) 
		points.append(newpoint)
		transformedpoints.append(transformedpoint)

	# Noise

	noisefrac=100 # 1 in every n is noisy
	noisy = random.sample(range(N),N/noisefrac)

	for j in noisy:
		correctLabels[j]*=-1

	input = np.array(transformedpoints)
	output = np.array(correctLabels)
	weights = np.dot(np.dot(np.linalg.inv(np.dot(input.T,input)),input.T),output)
	ein=0.0
	for j in range(N):
		if label(weights,transformedpoints[j])!=correctLabels[j]:
			ein+=1

	ein/=N
	avgein+=ein

	eout=0.0
	testpoints=[]
	transformedtestpoints=[]
	testLabels=[]
	for j in range(1000):
		testpoint=np.array(([1,point(),point()]))
		x=testpoint[1]
		y=testpoint[2]
		transformedtestpoint=[1,x,y,x*y,x*x,y*y]
		testLabels.append( np.sign(pow(x,2)+pow(y,2)-0.6))
		transformedtestpoints.append(transformedtestpoint)

	noisy = random.sample(range(1000),1000/noisefrac)

	for j in noisy:
		testLabels[j]*=-1

	for j in range(1000):
		if label(weights,transformedtestpoints[j])!=testLabels[j]:
			eout+=1

	eout/=1000
	avgeout+=eout
	print(i)

avgeout/=runs
avgein/=runs
print(avgein)
print(avgeout)
print(weights)