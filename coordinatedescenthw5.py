import math

def error(u,v):
	return (pow(u*math.exp(v)-2*v*math.exp(-u),2))

def errordu(u,v):
	return (2*(u*math.exp(v)-2*v*math.exp(-u))*(math.exp(v)+2*v*math.exp(-u)))

def errordv(u,v):
	return (2*(u*math.exp(v)-2*v*math.exp(-u))*(u*math.exp(v)-2*math.exp(-u)))

u=1
v=1
learning=0.1

for i in range(15):
	u=u-learning*errordu(u,v)
	v=v-learning*errordv(u,v)

print(error(u,v))

