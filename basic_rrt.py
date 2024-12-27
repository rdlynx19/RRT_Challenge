import random
import math
import copy
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.collections import LineCollection

#  Edit citations 
tree = []

# children = {q_init : []}

def algo_rrt(q_init, K, D = 100, delta = 1):
    children = {q_init : []}
    t = 0
    while t < K:
        random.seed(None)
        q_rand = (random.random() * D, random.random() * D)

        if len(tree)<1:
            tree.append(q_init)
            continue

        dist_min = 100000
        closest_neighbor = 0
        for node in tree:
            check_dist = (q_rand[0]- node[0])**2 + (q_rand[1]- node[1])**2
            if (check_dist < dist_min):
                dist_min = check_dist
                closest_neighbor = copy.deepcopy(node)

        disp_vecX = (q_rand[0] - closest_neighbor[0])/math.sqrt(dist_min) * delta# Multiply with delta if delta is not equal to one
        disp_vecY = (q_rand[1] - closest_neighbor[1])/math.sqrt(dist_min) * delta

        q_new = (closest_neighbor[0] + disp_vecX, closest_neighbor[1] + disp_vecY)

        tree.append(q_new)
        children[q_new] = []
        if closest_neighbor in children.keys():
            children[closest_neighbor].append(q_new)
        


        t = t + 1
    branches = []
    collection = []
    for key in children.keys():
        branches.append(key)
        
        for val in children[key]:
            branches.append(val)
            
        collection.append(branches)
        branches = []
    
    fig, ax = plt.subplots(figsize = (10,10))
    ax.set_xlim(10,80)
    ax.set_ylim(10,80)
    ax.set_xlabel("X")
    ax.set_ylabel("Y") 
    
    line_collection = LineCollection(collection)

    initial_line = ax.plot([], [], color='blue', alpha = 0.5, label='Edges')[0]
    initial_scatter = ax.scatter([],[], color='blue', label='Nodes')

    plt.legend()

    for line in line_collection.get_segments():
        ax.scatter(line[:,0], line[:,1], color='blue' )
        ax.plot(line[:,0], line[:,1], color='blue', alpha = 0.5)
        plt.pause(0.01)
    
    plt.show()
    


algo_rrt((50,50),500)

