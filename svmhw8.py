from sklearn.svm import SVC	
import numpy as np 
import random as rnd
from collections import Counter

class supportvectormachine:
 	'End to end svm class'

 	def __init__(self, kernel='rbf', C=1, coeff=0, degree=3, gamma =1 ):
 		self.kernel = kernel
 		self.C = C
 		self.coeff = coeff
 		self.degree = degree
 		self.gamma = gamma
 		self.classifier= SVC(self.C, self.kernel,self.degree, self.gamma, self.coeff)

 	def updatekernel(self,kernel):
 		self.kernel = kernel
 		self.classifier= SVC(self.C, self.kernel,self.degree, self.gamma, self.coeff)

 	def updateC(self,C):
 		self.C = C
 		self.classifier= SVC(self.C, self.kernel,self.degree, self.gamma, self.coeff)

 	def updatecoeff(self,coeff):
 		self.coeff = coeff
 		self.classifier= SVC(self.C, self.kernel,self.degree, self.gamma, self.coeff)

 	def updatedegree(self,degree):
 		self.degree = degree
 		self.classifier= SVC(self.C, self.kernel,self.degree, self.gamma, self.coeff)

 	def updategamma(self,gamma):
 		self.gamma = gamma
 		self.classifier= SVC(self.C, self.kernel,self.degree, self.gamma, self.coeff)

 	def trainset(self,traindata):
 		self.traindata = traindata

 	def testset(self,testdata):
 		self.testdata = testdata

 	def model(self):
 		print "Kernel: ", self.kernel, "\nPenalty Parameter: ", self.C, "\nDegree of Poly Kernel: ", self.degree, " \nKernel coefficient: ", self.gamma, "\nIndependant term in kernel: ", self.coeff

 	def printtrain(self):
 		print(self.traindata)

 	def onevsall(self,digit):
 		for i in range(np.shape(self.traindata)[0]):
 			if self.traindata[i,0]==digit:
 				self.traindata[i,0]=1
 			else:
 				self.traindata[i,0]=-1

 		for i in range(np.shape(self.testdata)[0]):
 			if self.testdata[i,0]==digit:
 				self.testdata[i,0]=1
 			else:
 				self.testdata[i,0]=-1

 	def onevsone(self,digit1,digit2):
 		irrelevant=[]
 		for i in range(np.shape(self.traindata)[0]):
 			if self.traindata[i,0]==digit1:
 				self.traindata[i,0]=1
 			elif self.traindata[i,0]==digit2:
 				self.traindata[i,0]=-1 
 			else:
 				self.traindata[i,0]=0	
 				irrelevant.append(i)

 		self.traindata=np.delete(self.traindata,irrelevant,axis=0)

 		irrelevant=[]

 		for i in range(np.shape(self.testdata)[0]):
 			if self.testdata[i,0]==digit1:
 				self.testdata[i,0]=1
 			elif self.testdata[i,0]==digit2:
 				self.testdata[i,0]=-1 
 			else:
 				self.testdata[i,0]=0	
 				irrelevant.append(i)

 		self.testdata=np.delete(self.testdata,irrelevant,axis=0)

 	def train(self):
 		self.classifier.fit(self.traindata[:,1:],self.traindata[:,0])

 	def ein(self):
 		self.inprediction = self.classifier.predict(self.traindata[:,1:])
 		self.total = len(self.inprediction)
 		self.count=0.0
 		for i in range(self.total):
 			if(self.inprediction[i]!=self.traindata[i,0]):
 				self.count+=1

 		return self.count/self.total
 		#return self.classifier.score(self.traindata[:,1:],self.traindata[:,0])

 	def eout(self):
		self.outprediction = self.classifier.predict(self.testdata[:,1:])
		self.total = len(self.outprediction)
		self.count=0.0
		for i in range(self.total):
			if(self.outprediction[i]!=self.testdata[i,0]):
				self.count+=1

		return self.count/self.total
		#return self.classifier.score(self.testdata[:,1:],self.testdata[:,0])

	def nsv(self):
		return self.classifier.n_support_

	def partition(self,n): 
		lst = range(len(self.traindata))
		division = len(self.traindata) / float(n)
		rnd.shuffle(lst)
		return [ lst[int(round(division * i)): int(round(division * (i + 1)))] for i in xrange(n) ]

print("HW8 Exercises \n")

# Question 7/8

print("Question 7/8 \n")


runs=1
partitions=10
chosenC = []
allecv=np.array([ [0.0]*100 ]*5)

for i in range(runs):
	avgecv=[]
	for j in range(5):
		svm1 = supportvectormachine('poly', C=pow(10,-j), degree=2)
		training=np.genfromtxt("hw8train.txt")
		testing=np.genfromtxt("hw8test.txt")
		svm1.trainset(training)
		svm1.testset(testing)
		partitionindices=svm1.partition(partitions)
		ecv=0.0
		for k in range(partitions):
			training=np.genfromtxt("hw8train.txt")
			testing=np.genfromtxt("hw8test.txt")
			relindices=np.array([])
			trainparts=range(partitions)
			trainparts.pop(k)
			for l in trainparts:
				relindices=np.concatenate([relindices,partitionindices[l]])

			svm1.trainset(training[relindices.astype(int),:])
			svm1.testset(training[partitionindices[k],:])
			svm1.onevsone(1,5)
			svm1.train()
			ecv+=svm1.eout()

		avgecv.append(ecv/partitions)
		allecv[j][i]=ecv/partitions

	chosenC.append(pow(10,-avgecv.index(min(avgecv))))
	print "Run number:", i, "\n"

mode = Counter(chosenC).most_common(5)
print "Most common C:", mode[0][0],",", mode[0][1], "times"
print "All C's :", mode
print "Ecv values for decreasing C's:\n" , sum(allecv[0,:])/runs , sum(allecv[1,:])/runs , sum(allecv[2,:])/runs , sum(allecv[3,:])/runs , sum(allecv[4,:])/runs 


# Question 9/10

print("\nQuestion 9/10\n")

for i in [-2,0,2,4,6]:
	training=np.genfromtxt("hw8train.txt")
	testing=np.genfromtxt("hw8test.txt")
	svm1 = supportvectormachine('rbf', C=pow(10,i), gamma=1)
	svm1.trainset(training)
	svm1.testset(testing)
	svm1.onevsone(1,5)
	svm1.train()
	print "C:" , pow(10,i), ", Ein:", svm1.ein(), ", Eout:", svm1.eout(), ",Support Vectors:", sum(svm1.nsv())

print("\n")

# Question 5/6

print("Question 5/6")
print("Polynomial Kernel with degree 5\n")

for i in range(5):
	training=np.genfromtxt("hw8train.txt")
	testing=np.genfromtxt("hw8test.txt")
	svm1 = supportvectormachine('poly', C=pow(10,-i), degree=5)
	svm1.trainset(training)
	svm1.testset(testing)
	svm1.onevsone(1,5)
	svm1.train()
	print "C:" , pow(10,-i), ", Ein:", svm1.ein(), ", Eout:", svm1.eout(), ",Support Vectors:", sum(svm1.nsv())

print("\nPolynomial Kernel with degree 2\n")

for i in range(5):
	training=np.genfromtxt("hw8train.txt")
	testing=np.genfromtxt("hw8test.txt")
	svm1 = supportvectormachine('poly', C=pow(10,-i), degree=2)
	svm1.trainset(training)
	svm1.testset(testing)
	svm1.onevsone(1,5)
	svm1.train()
	print "C:" , pow(10,-i), ", Ein:", svm1.ein(), ", Eout:", svm1.eout(), ",Support Vectors:", sum(svm1.nsv())

print("\n")

# Question 2/3/4

print("Question 2/3/4\n")

for i in range(10):
	training=np.genfromtxt("hw8train.txt")
	testing=np.genfromtxt("hw8test.txt")
	svm1 = supportvectormachine('poly', C=0.01, degree=2)
	svm1.trainset(training)
	svm1.testset(testing)
	svm1.onevsall(i)
	svm1.train()
	print i, "vs all,", "Ein:", svm1.ein(), ", Eout:", svm1.eout(), ",Support Vectors:", sum(svm1.nsv())



