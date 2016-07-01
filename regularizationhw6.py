import numpy as np 
import csv


def label(weights,input):
	return np.sign(weights.dot(input))

traindata=np.genfromtxt("hw6in.csv")
testdata=np.genfromtxt("hw6out.csv")			

numtrain=35
numtest=250				

inputlabels=traindata[:,2]
transformedtraindata=np.array([0,0,0,0,0,0,0,0])
for i in range(numtrain):
	x1=traindata[i,0]
	x2=traindata[i,1]
	transform=np.array([1,x1,x2,pow(x1,2),pow(x2,2),x1*x2,abs(x1-x2),abs(x1+x2)])
	transformedtraindata=np.vstack((transformedtraindata,transform))

transformedtraindata=transformedtraindata[1:,:]

weights = np.dot(np.dot(np.linalg.inv(np.dot(transformedtraindata.T,transformedtraindata)),transformedtraindata.T),inputlabels)
	
ein=0.0

for i in range(numtrain):
	if label(weights,transformedtraindata[i,:])!=inputlabels[i]:
		ein+=1

ein/=numtrain
print(ein)

outputlabels=testdata[:,2]
transformedtestdata=np.array([0,0,0,0,0,0,0,0])
for i in range(numtest):
	x1=testdata[i,0]
	x2=testdata[i,1]
	transform=np.array([1,x1,x2,pow(x1,2),pow(x2,2),x1*x2,abs(x1-x2),abs(x1+x2)])
	transformedtestdata=np.vstack((transformedtestdata,transform))

transformedtestdata=transformedtestdata[1:,:]
eout =0.0
for i in range(numtest):
	if label(weights,transformedtestdata[i,:])!=outputlabels[i]:
		eout+=1

eout/=numtest
print(eout)

print(weights)