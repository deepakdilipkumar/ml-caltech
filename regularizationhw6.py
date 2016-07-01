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
    traindata.append(row) 	
    numtrain+=1							
traindata = np.array(traindata) 	

for row in test_file: 							
    testdata.append(row[0:]) 	
    numtest+=1							
testdata = np.array(testdata) 									

inputlabels=traindata[,2]

for i in range(numtrain):
	x1=traindata[i,0]
	x2=traindata[i,1]

	transform=np.array([1,x1,x2,pow(x1,2),pow(x2,2),x1*x2,abs(x1-x2),abs(x1+x2)])
	transformedtraindata.append(transform)

weights = np.dot(np.dot(np.linalg.inv(np.dot(transformedtraindata.T,transformedtraindata)),transformedtraindata.T),inputlabels)
	
ein=0

for i in range(numtrain):
	if label(weights,transformedtraindata[i,0:2])!=inputlabels[i]:
		ein+=1

ein/=numtrain
print(ein)

outputlabels=testdata[,2]
for i in range(numtest):
	x1=testdata[i,0]
	x2=testdata[i,1]

	transform=np.array([1,x1,x2,pow(x1,2),pow(x2,2),x1*x2,abs(x1-x2),abs(x1+x2)])
	transformedtestdata.append(transform)

eout =0
for i in range(numtest):
	if label(weights,transformedtestdata[i,0:2])!=outputlabels[i]:
		eout+=1

eout/=numtest
print(eout)

print(weights)