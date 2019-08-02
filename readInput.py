import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import stats


def inputNodes(): 
	# what each data point is called:
	names = ["football","baseball","basketball","tennis","softball","canoeing","handball","rugby","hockey","ice hockey","swimming","track","boxing","volleyball","lacrosse","skiing","golf","polo","surfing","wrestling","gymnastics"]

	 # load the csv provided on bcourses
	similarities = np.loadtxt(open("similarities.csv", "rb"), delimiter=",", skiprows=1)

	distCalc = lambda t: 1-t
	distances = np.array([distCalc(xi) for xi in similarities]) ## *FILL IN* - How should we convert similarities to distances?
	D = 2 # How many dimensions we are go)ing to use
	N = distances.shape[0] # the number of items
	#assert(distances.shape[1] == N and N==len(names)) # be sure we loaded as many items as we have names for

	# Pick a position for each point. Note this is an NxD matrix
	# so that pos[11,1] is the y coordinate for the 11th item
	# and pos[11] is a (row) vector for the position of the 11th item
	pos = np.random.normal(0.0,1.0,size=(N,D))

	y = [row[1] for row in pos]
	x = [row[0] for row in pos]
	n = ["football","baseball","basketball","tennis","softball","canoeing","handball","rugby","hockey","ice hockey","swimming","track","boxing","volleyball","lacrosse","skiing","golf","polo","surfing","wrestling","gymnastics"]

	#fig, ax = plt.subplots()
	#for i, txt in enumerate(n):
	#    ax.annotate(txt, (x[i], y[i]))
	#ax.scatter(x, y)
	#plt.title("Random positions (before MDS)")
	#plt.xlabel("X distance")
	#plt.ylabel("Y distance")
	#plt.show()
	return pos, distances, N, D
