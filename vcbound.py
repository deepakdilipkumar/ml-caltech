import math
import matplotlib

def growth(N,d):
	return pow(N,d)

def vc(N,del,d):
	return math.sqrt(8*math.log(4*growth(2*N,d)/del)/N)

def rademacher(N,del,d):
	return (math.sqrt(2*math.log(2*N*growth(N,d))/N)+math.sqrt(2*math.log(1/del)/N)+1/N)