import random as rnd
import numpy
#import matplotlib.pyplot as plt

def minIndex(list):
	minimum= min(list)
	for i in range(len(list)):
		if (list[i]==minimum):
			return i

nu1=[]
nuRand=[]
nuMin=[]
for k in range(100000):
	headFreq=[]
	for i in range(1000):
		heads=0.0
		for j in range(10):
			if(rnd.choice([0,1])==1):
				heads+=1

		headFreq.append(heads/10)

	nu1.append(headFreq[0])
	nuRand.append(headFreq[rnd.choice(range(1000))])
	nuMin.append(headFreq[minIndex(headFreq)])
	print(k)

print(sum(nuMin)/100000)
nu1Dist=numpy.histogram(nu1,bins=11)
nuRandDist=numpy.histogram(nuRand,bins=11)
nuMinDist=numpy.histogram(nuMin,bins=11)
print(nu1Dist[0])
print(nuRandDist)
print(nuMinDist)