import numpy as np 
import math
import random as rnd

def layersize(l):
	return layersizearray[l]

def nl(x): # Non-linearity
	return math.tanh(x)

layersizearray = [2,2,2,1]			# Input, Hidden layers, output
numlayers=3
learning=0.1
maxnodes=max(layersizearray)

w = [ [ [0]* (numlayers+1) ] * (maxnodes+1) ] * (maxnodes+1)
x = [ [0]* (numlayers+1)] * (maxnodes+1)
#x[:][0]=inputfeatures
delta = [ [0]* (numlayers+1)] * (maxnodes+1)

for l in range(numlayers)[1:]:
	for i in range(layersize(l-1)):
		for j in range(layersize(l)):
			w[i][j][l] = rnd.uniform(-0.2,0.2)
			
for l in range(numlayers)[1:]:
	for j in range(layersize(l)):
		signal=0
		for i in range(layersize(l-1)):
			signal+=x[i][l-1]*w[i][j][l-1]

		x[j][l]=nl(signal)
