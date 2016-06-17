import math
import matplotlib.pyplot as plt 
import numpy as np

def growth(N,d):
	return pow(N,d)

def vc(N,delta,d):
	return math.sqrt(8*math.log(4*growth(2*N,d)/delta)/N)

def rademacher(N,delta,d):
	return (math.sqrt(2*math.log(2*N*growth(N,d))/N)+math.sqrt(2*math.log(1/delta)/N)+1/N)

def parrondo(N,delta,d):
	eps = 0
	old = 1
	tol=0.001
	while (abs(eps-old)>tol):
		old=eps
		eps=math.sqrt((2*eps+math.log(6*growth(2*N,d)/delta))/N)

	return eps

def devroye(N,delta,d):
	eps = 0
	old = 1
	tol=0.001
	while (abs(eps-old)>tol):
		old=eps
		eps=math.sqrt((4*eps*(1+eps)+math.log(4/delta)+d*math.log(pow(N,2)))/(2*N))

	return eps


N=10000
delta=0.05
d=50

epsvc=[]
epsrademacher=[]
epsparrondo=[]
epsdevroye=[]

for i in range(N):
	epsvc.append(vc((i+1)*10,delta,d))
	epsrademacher.append(rademacher((i+1)*10,delta,d))
	epsparrondo.append(parrondo((i+1)*10,delta,d))
	epsdevroye.append(devroye((i+1)*10,delta,d))

x=(np.array(range(N))+1)*10
plt.plot(x,epsvc)
plt.plot(x,epsrademacher)
plt.plot(x,epsparrondo)
plt.plot(x,epsdevroye)

print(epsvc[N-1])
print(epsrademacher[N-1])
print(epsparrondo[N-1])
print(epsdevroye[N-1])
