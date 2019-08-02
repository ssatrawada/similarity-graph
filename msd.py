import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import stats
import msd_helperMethods 
import readInput
#represents the initial random positions of the nodes 
def runMsd(pos, distances):

	old = msd_helperMethods.compute_full_gradient(pos)
	old_stress = msd_helperMethods.stress(old)
	new = msd_helperMethods.compute_full_gradient(old)
	new_stress = msd_helperMethods.stress(new)
	array_stress = np.array([old_stress, new_stress ])
	count = 2
	#i = 0
	while(old_stress - new_stress > 0.001):
	    old = new 
	    old_stress = msd_helperMethods.stress(old)
	    new = msd_helperMethods.compute_full_gradient(old)
	    new_stress = msd_helperMethods.stress(new)
	    array_stress = np.append(array_stress, new_stress)
	    #i+=1
	    #if(i%10 == 0):
	    #    print(new_stress)
	    count+=1
	pos = new
	#print(new_stress)

	y = [row[1] for row in pos]
	x = [row[0] for row in pos]
	n = ["football","baseball","basketball","tennis","softball","canoeing","handball","rugby","hockey","ice hockey","swimming","track","boxing","volleyball","lacrosse","skiing","golf","polo","surfing","wrestling","gymnastics"]

	fig, ax = plt.subplots()
	for i, txt in enumerate(n):
	    ax.annotate(txt, (x[i], y[i]))
	ax.scatter(x, y)
	plt.title("Postitions after MDS)")
	plt.xlabel("X distance")
	plt.ylabel("Y distance")
	plt.show()
	return pos, array_stress, count