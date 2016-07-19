import numpy as np 
import random as rnd

class regularizedlr:
 	'End to end svm class'

 	def __init__(self, regpar=1):
 		self.regpar = regpar

 	def updateregpar(self, regpar):
 		self.regpar = regpar

 	def trainset(self,traindata):
 		self.traindata = traindata

 	def testset(self,testdata):
 		self.testdata = testdata

 	def model(self):
 		print "Regularization Parameter: ", self.regpar

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
 		

 	def ein(self):


 	def eout(self):






