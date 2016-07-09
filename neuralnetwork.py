import numpy as np 
import math

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
delta = [ [0]* (numlayers+1)] * (maxnodes+1)