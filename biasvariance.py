import numpy as np
import random
import math

def point():
	return random.uniform(-1,1)

def f(x):
	return math.sin(math.pi*x)

def g(x1,x2):
	return ((x1*f(x1)+x2*f(x2))/(pow(x1,2)+pow(x2,2)))


numdata=100000
a=[]

for i in range(numdata):
	x1 = point()
	x2 = point()
	a.append(g(x1,x2))

abar = sum(a)/len(a) 
print(abar)

numbias = 100000
errbias =0

for i in range(numbias):
	x = point()
	errbias+= pow(abar*x-f(x),2)

errbias/=numbias
print(errbias)
