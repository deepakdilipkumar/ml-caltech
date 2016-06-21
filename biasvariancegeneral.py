import numpy as np
import random
import math

def point():
	return random.uniform(-1,1)

def f(x):
	return math.sin(math.pi*x)

def a(x1,x2):														
	#return ((x1*f(x1)+x2*f(x2))/(pow(x1,2)+pow(x2,2)))					# Parameter minimizing mean squared error for given dataset of 2 points for g=ax
	#return 0															# g=b
	#return ((f(x2)-f(x1))/(x2-x1))										# g=ax+b
	#return ((pow(x1,2)*f(x1)+pow(x2,2)*f(x2))/(pow(x1,4)+pow(x2,4)))	# g=ax^2
	return (f(x2)-f(x1))/(pow(x2,2)-pow(x1,2))							# g=ax^2 +b

def b(x1,x2):
	#return 0 														# g=ax
	#return (f(x1)+f(x2))/2											# g=b
	#return ((f(x1)*x2-f(x2)*x1)/(x2-x1))							# g=ax+b
	#return 0														# g=ax^2
	return (f(x1)*pow(x2,2)-f(x2)*pow(x1,2))/(pow(x2,2)-pow(x1,2))	# g=ax^2+b

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
check=[]
c=[]

for i in range(numx):
	x = point()
	errbias+= pow(abar*pow(x,2)+bbar-f(x),2)
	errvar = 0 
#	errbias+= pow(abar*x+bbar-f(x),2)
	for j in range(numd):
		x1=point()
		x2=point()
		errvar+=pow(a(x1,x2)*pow(x,2)+b(x1,x2)-abar*pow(x,2)-bbar,2)
#		errvar+=pow(a(x1,x2)*x+b(x1,x2)-abar*x-bbar,2)

	#print(i)
	errvar/=numd
	check.append(errvar)
	c.append(x)
	var+=errvar

bias=errbias/numx
print(bias)

var/=numx
print(var)
eout=bias+var
print(eout)

print(c[check.index(max(check))])