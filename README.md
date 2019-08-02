# similarity-graph
Utilizes multidimensional scaling in order to find an arrangement of points given a list of nouns. The distances between the two items in the resulting graph correspond to how similar the nodes are given similarity ratios. 

MDS algorithm: MDS starts with a similarity matrix and works towards finding placements for points such that the distances between the points matches how similar the points are. In order to run this algorithm, the variable stress is used to measure how different the distances between two points are to how similar they are. 

Stress is calculated by the square difference between all the points distance and their similarities. 

In order to minimize the stress, we compute the gradient to learn which direction to improve by. 


Descriptions for Graphs returned after running: python3 run.py: 
	* These graphs can also be found in the imagesOfGraphs folder 
    1) RandomPositions-beforeMDS: This graph shows the locations of the nodes in relation to one other at the beginning of the algorithm. In this step, the locations are randomized which can be seen since distance and similarity of the nodes are not correlated. 

    2) PositionsAfterMDS: This graph shows the locations of the nodes after MDS has completed. This can be seen since nodes that are similar (ex: swimming and surfing) will be next to each other 

    3) Predictions-vs-Accurate: This graph plots a point for each pair of nodes where the x value is the weight of similarity given as input and the y value is the weight predicted through the algorithm. As can be seen, the graph has a linear trend close to y = x proving that the algorithm is doing its job. 

    4) StressOverIterationsofMDS: This graph shows how the stress between the nodes reduc as more iterations of MDS are run. As you can see at some point there is no use doing more iterations since the stress level is minimized and constant.  (Past 40 iterations) 

  
