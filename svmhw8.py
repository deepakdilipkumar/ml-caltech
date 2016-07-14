from sklearn.svm import SVC	
import numpy as np 

class supportvectormachine:
 	'End to end svm class'

 	def __init__(self, kernel='rbf', C=1, coeff=1, degree=3, gamma =1 ):
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
 			if self.traindata[i][0]==digit:
 				self.traindata[i][0]=1
 			else:
 				self.traindata[i][0]=-1

 	def onevsone(self,digit1,digit2):
 		for i in range(np.shape(self.traindata)[0]):
 			if self.traindata[i][0]==digit1:
 				self.traindata[i][0]=1
 			elif self.traindata[i][0]==digit2:
 				self.traindata[i][0]=-1 
 			else:
 				self.traindata[i][0]=0	

 	def train(self):
 		self.classifier.fit(self.traindata[:,1:],self.traindata[:,0])

 	def ein(self):
 		self.inprediction = self.classifier.predict(self.traindata[:,1:])
 		total = len(self.inprediction)
 		count=0.0
 		for i in range(total):
 			if(self.inprediction[i]!=self.traindata[i,0]):
 				count+=1

 		return count/total

 	def eout(self):
		self.outprediction = self.classifier.predict(self.testdata[:,1:])
		total = len(self.outprediction)
		count=0.0
		for i in range(total):
			if(self.outprediction[i]!=self.testdata[i,0]):
				count+=1

		return count/total




traindata=np.genfromtxt("hw8train.txt")
testdata=np.genfromtxt("hw8test.txt")

svm1 = supportvectormachine('rbf', 1, 1, 10, 1)
svm1.trainset(traindata)
svm1.testset(testdata)
svm1.model()
#svm1.printtrain()
svm1.train()
print(svm1.ein())
print(svm1.eout())

