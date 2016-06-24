import math

def error(u,v):
	return (pow(u*math.exp(v)-2*v*math.exp(-u),2))

def errordu(u,v):
	return (2*(u*math.exp(v)-2*v*math.exp(-u))*(math.exp(v)+2*v*math.exp(-u)))

def errordv(u,v):
	return (2*(u*math.exp(v)-2*v*math.exp(-u))*(u*math.exp(v)-2*math.exp(-u)))

tolerance=1e-14
u=1
v=1
learning=0.1
runs=0

while(error(u,v)>tolerance):
	curu=u
	curv=v
	u=u-learning*errordu(curu,curv)
	v=v-learning*errordv(curu,curv)
	runs+=1

print(runs)
print(u)
print(v)
