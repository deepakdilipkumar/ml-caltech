import numpy as np
import random
import math

def point():
	return random.uniform(-1,1)

def f(x):
	return math.sin(math.pi*x)

def a(x1,x2):													
	#return ((x1*f(x1)+x2*f(x2))/(pow(x1,2)+pow(x2,2)))			# Parameter minimizing mean squared error for given dataset of 2 points for g=ax
	return 0

def b(x1,x2):
	return (f(x1)+f(x2))/2										# b in g=b

numdata=100000
abar=0
bbar=0

for i in range(numdata):
	x1 = point()
	x2 = point()
	abar+=a(x1,x2)
	bbar+=b(x1,x2)
	#a.append(a(x1,x2))
	#b.append(b(x1,x2))

abar/=numdata
bbar/=numdata

print(abar)
print(bbar)

numx= 1000						# Expectation over large number of inputs x
errbias =0
errvar=0
numd=1000
var=0
bias=0

for i in range(numx):
	x = point()
	errbias+= pow(abar*x-f(x),2)
	for j in range(numd):
		x1=point()
		x2=point()
		errvar+=pow(a(x1,x2)*x+b(x1,x2)-abar*x-bbar,2)

	#print(i)
	errvar/=numd
	var+=errvar


bias=errbias/numx
print(bias)

var/=numx
print(var)
eout=bias+var
print(eout)