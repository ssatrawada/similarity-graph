import numpy as np
import sys
import matplotlib.pyplot as plt
from scipy import stats
import readInput 
import msd_helperMethods
import msd 
import msd_analysis


def main():
	msd_analysis.show_random_initial_graph()
	pos1, distances, N, D = readInput.inputNodes()

	msd_helperMethods.setDistance(distances)

	pos, array_stress, count = msd.runMsd(pos1, distances)



	msd_analysis.diff_msd_versus_inputWeights(pos, distances)



	msd_analysis.howManyItersOfMSD(array_stress, count)

	print("Program Finished")

	#This takes longer to run, but displays a more accurate 
		#representation of the final result 
	#msd_analysis.bestOf3(N, D)

if __name__ == "__main__":
    main()

	


