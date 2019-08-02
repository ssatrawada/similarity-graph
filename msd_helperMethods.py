import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import stats
import readInput 

distances = -1
def setDistance(distance): 
	global distances
	distances = distance

def dist(a,b):
    # Compute the Euclidean distance between two locations (numpy arrays) a and b
    # Thus, dist(pos[1], pos[2]) gives the distance between the locations for items 1 and 2
    ## *FILL IN*
    return (((a[0] - b[0])**2 + (a[1] -  b[1])**2)**(0.5))

def stress(p):
    # Take a matrix of positions (called here "p") and return the stress
    #matrix = np.array(p)
    sum1 = 0
    for i in range(0, len(p)): 
        for j in range(i, len(p)):
                #print(p[i])
                if(i !=j):
                    sum1 += (distances[i][j]- dist(p[i], p[j]))**2
    return sum1

def add_delta(p, i, d, delta):
    # This is a helper function that will make a new vector which is the same as p (a position matrix), except that
    # p[i,d] has been increased by delta (which may be positive or negative)
    #matrix = np.array(p)
    p[i, d] += delta
    return p

def compute_gradient(p, i,d, delta = 0.001):
    # compute the gradient of the stress function with repect to the [i,d] entry of a position matrix p
    # (e.g. the derivative of stress with respect to the i'th coordinate of the x'th dimension)
    # Here, to compute numerically, you can use the fact that
    # f'(x) = (f(x+delta)-f(x-delta))/(2 delta) as delta -> 0
    #matrix = np.array(p)
    stepsize=0.01
    ## *FILL IN* gradient*stepsize
    #yourspot-gradient*stepsize
    stress_x_plus = stress(add_delta(p, i, d, delta))
    stress_x_minue = stress(add_delta(p, i, d, -1*delta))
    gradient =  (stress_x_plus - stress_x_minue )/(2*delta)
    return gradient

def compute_full_gradient(p):
    # Numerically compute the full gradient of stress at a position p
    # This should return a matrix whose elements are the gradient of stress at p with respect to each [i,d] coordinate
    # p.shape = 0 
    ## *FILL IN* compute_gradiant.p_shape 
    stepsize=0.01
    #matrix = np.array(p)
    for i in range(0, len(p)):
        d1 = p[i, 0] - compute_gradient(p, i, 0)*stepsize
        d2 = p[i, 1] - compute_gradient(p, i, 1)*stepsize
        p[i, 0] = d1
        p[i, 1] = d2
    return p
            