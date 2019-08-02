#run individual methods here to see plots showing various insight into the data 
import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import stats
import readInput 
import msd_helperMethods
import msd 


def show_random_initial_graph(): 
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

	fig, ax = plt.subplots()
	for i, txt in enumerate(n):
	   ax.annotate(txt, (x[i], y[i]))
	ax.scatter(x, y)
	plt.title("Random positions (before MDS)")
	plt.xlabel("X distance")
	plt.ylabel("Y distance")
	plt.show()

def diff_msd_versus_inputWeights(pos, distances): 
	person_arr = np.array([])
	for i in range(0, len(distances)): 
	    for j in range(i, len(distances)):
	         person_arr = np.append(person_arr,distances[i][j] )
	len(person_arr)

	mds_arr = np.array([])
	for i in range(0, len(pos)): 
	        for j in range(i, len(pos)):
	            mds_arr = np.append(mds_arr, msd_helperMethods.dist(pos[i], pos[j]))

	slope, intercept, r_value, p_value, std_err = stats.linregress(mds_arr, person_arr)
	line = slope*mds_arr+intercept

	plt.plot(mds_arr,person_arr,'o', mds_arr, line)
	#plt.plot(person_arr, mds_arr, 'bo')

	plt.title("Pairwise Distances MDS found vs. People’s Reported Distances")
	plt.xlabel("Pairwise Distances MDS found")
	plt.ylabel("People’s Reported Distances")
	plt.show()

def howManyItersOfMSD(array_stress, count): 
	
	plt.plot(np.array(range(0, count)), array_stress)
	plt.title("Stress over iterations of MDS")
	plt.xlabel("Number of Iterations")
	plt.ylabel("Stress")
	plt.show()

#This method uses howManyItersofMSD() and runs MSD five times 
def bestOf3(N, D): 
	pos = np.random.normal(0.0,1.0,size=(N,D))
	minNewStress = 10000
	minNew = pos
	for i in range(0, 3):
	    pos = np.random.normal(0.0,1.0,size=(N,D))
	    old = msd_helperMethods.compute_full_gradient(pos)
	    old_stress = msd_helperMethods.stress(old)
	    new = msd_helperMethods.compute_full_gradient(old)
	    new_stress = msd_helperMethods.stress(new)
	    array_stress = np.array([old_stress, new_stress ])
	    count = 2
	    #i = 0
	    while(old_stress - new_stress > 0.0001):
	        old = new 
	        old_stress = msd_helperMethods.stress(old)
	        new = msd_helperMethods.compute_full_gradient(old)
	        new_stress = msd_helperMethods.stress(new)
	        array_stress = np.append(array_stress, new_stress)
	        count+=1
	    print(new_stress)
	    if(minNewStress > new_stress):
	        minNewStress = new_stress
	        minNew = new
	pos = minNew
	print(minNewStress)
	y = [row[1] for row in pos]
	x = [row[0] for row in pos]
	n = ["football","baseball","basketball","tennis","softball","canoeing","handball","rugby","hockey","ice hockey","swimming","track","boxing","volleyball","lacrosse","skiing","golf","polo","surfing","wrestling","gymnastics"]
	fig, ax = plt.subplots()
	for i, txt in enumerate(n):
	    ax.annotate(txt, (x[i], y[i]))
	ax.scatter(x, y)
	plt.title("Postitions of the best of 5 MDS iterations)")
	plt.xlabel("X distance")
	plt.ylabel("Y distance")
	plt.show()



