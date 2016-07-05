import numpy as np 
import matplotlib.pyplot as plt

def label(weights,input):
	return np.sign(weights.dot(input))

traindata=np.genfromtxt("hw6in.csv")
testdata=np.genfromtxt("hw6out.csv")			

numtrain=np.shape(traindata)[0]
numtest=np.shape(testdata)[0]			

inputlabels=traindata[:,2]
transformedtraindata=np.array([0,0,0,0,0,0,0,0])
for i in range(numtrain):
	x1=traindata[i,0]
	x2=traindata[i,1]
	transform=np.array([1,x1,x2,pow(x1,2),pow(x2,2),x1*x2,abs(x1-x2),abs(x1+x2)])
	transformedtraindata=np.vstack((transformedtraindata,transform))

transformedtraindata=transformedtraindata[1:,:]

outputlabels=testdata[:,2]
transformedtestdata=np.array([0,0,0,0,0,0,0,0])
for i in range(numtest):
	x1=testdata[i,0]
	x2=testdata[i,1]
	transform=np.array([1,x1,x2,pow(x1,2),pow(x2,2),x1*x2,abs(x1-x2),abs(x1+x2)])
	transformedtestdata=np.vstack((transformedtestdata,transform))

transformedtestdata=transformedtestdata[1:,:]

einlist=[]
eoutlist=[]
klist=[]
trainindex=25


for i in [3,4,5,6,7]:
	validation = transformedtraindata[0:trainindex,0:i]
	train = transformedtraindata[trainindex:,0:i]
	validationlabels=inputlabels[0:trainindex]
	trainlabels=inputlabels[trainindex:]
	weights = np.dot(np.dot(np.linalg.inv(np.dot(train.T,train)),train.T),trainlabels)
		
	ein=0.0
	for j in range(len(validationlabels)):
		if label(weights,validation[j,:])!=validationlabels[j]:
			ein+=1

	ein/=len(validationlabels)
	einlist.append(ein)
	#print(ein)

	eout =0.0
	for j in range(numtest):
		if label(weights,transformedtestdata[j,0:i])!=outputlabels[j]:
			eout+=1

	eout/=numtest
	eoutlist.append(eout)
#print(eout)

#plt.plot(klist,einlist,'r--',klist,eoutlist,'bs')
#plt.show()

print(einlist)
print(eoutlist)