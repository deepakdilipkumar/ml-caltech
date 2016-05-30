import random as rnd
import matplotlib.pyplot as plt

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
	nuMin.append(minIndex(headFreq))
	print(k)

print(sum(nuMin)/100000)
plt.hist(nu1)
plt.hist(nuRand)
plt.hist(nuMin)