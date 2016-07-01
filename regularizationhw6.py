import numpy as np 
import csv


def label(weights,input):
	return np.sign(weights.dot(input))


train_file = csv.reader(open('hw6in.csv', 'rb')) 	
test_file = csv.reader(open('hw6out.csv', 'rb')) 	
traindata=[] 	
testdata=[]											

numtrain=0
numtest=0

for row in train_file: 							
    traindata.append(row[0:]) 								
traindata = np.array(data) 	

for row in test_file: 							
    testdata.append(row[0:]) 								
testdata = np.array(data) 									


for i in range(runs):

	
	for j in range(N):
		newpoint=np.array(([1,point(),point()]))
		x=newpoint[1]
		y=newpoint[2]
		transformedpoint=[1,x,y,x*y,x*x,y*y]
		correctLabels.append( np.sign(pow(x,2)+pow(y,2)-0.6)) 
		points.append(newpoint)
		transformedpoints.append(transformedpoint)

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