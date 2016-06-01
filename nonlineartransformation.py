import numpy as np 
import random

def point():
	return (random.uniform(-1,1))

def label(weights,input):
	return np.sign(weights.dot(input))

N=100
runs=1000
avgein=0.0

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
		correctLabels.append( np.sign(pow(x,2)+pow(y,2)-0.6)) #np.sign(newpoint[2]-slope*newpoint[1]-intercept)
		points.append(newpoint)
		transformedpoints.append(transformedpoint)

	# Noise

	noisy = random.sample(range(N),N/10)

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

	print(i)

avgein/=runs
print(avgein)
print(weights)