import numpy as np
import random
import math

def point():
	return random.uniform(-1,1)

def f(x):
	return math.sin(math.pi*x)

def g(x1,x2):													# Returns parameter a in g=ax
	return ((x1*f(x1)+x2*f(x2))/(pow(x1,2)+pow(x2,2)))			# Parameter minimizing mean squared error for given dataset of 2 points

numdata=100000
a=[]

for i in range(numdata):
	x1 = point()
	x2 = point()
	a.append(g(x1,x2))

a=np.array(a)
abar = sum(a)/len(a) 				# Parameter for gbar
print(abar)

numx= 100000						# Expectation over large number of inputs x
errbias =0
ex2 = 0

for i in range(numx):
	x = point()
	errbias+= pow(abar*x-f(x),2)
	ex2+=pow(x,2)

bias=errbias/numx
ex2/=numx
print(bias)

var=ex2*sum(pow(a-abar,2))/len(a)
print(var)
eout=bias+var
print(eout)