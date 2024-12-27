import random
import math
import copy
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Circle
from matplotlib.collections import LineCollection

#  Edit citations 
tree = []

# children = {q_init : []}

def check_collision(q_new, closest_neighbor,circle_collection,dist_min, flag = 0):
    for circ in circle_collection:
            x3 = circ.center[0]
            y3 = circ.center[1]

            # checking if either of the points lie inside the circle
            if((q_new[0] - x3)**2 + (q_new[1]-y3)**2 - (circ.radius)**2 < 0):
                flag = 1
                break
            if((closest_neighbor[0]-x3)**2 + (closest_neighbor[1]-y3)**2 - (circ.radius)**2 < 0):
                flag = 1
                break

############ Begin_Citation [4] ##############
            u = (((x3 - closest_neighbor[0])*(q_new[0]-closest_neighbor[0])) + ((y3 - closest_neighbor[1])*(q_new[1]-closest_neighbor[1])))/(dist_min)**2
            n_x = closest_neighbor[0] + u*(q_new[0]-closest_neighbor[0])
            n_y = closest_neighbor[1] + u*(q_new[1]-closest_neighbor[1])
############ End_Citation [4] ###############

############ Begin_Citation [5] ################
            if(0<=u<=1):
                normal_dist = math.sqrt((n_x - x3)**2 + (n_y - y3)**2) 
            else:
                closest_c = math.sqrt((x3 - closest_neighbor[0])**2 + (y3 - closest_neighbor[1])**2)
                q_c = math.sqrt((x3 - q_new[0])**2 + (y3 - q_new[1])**2)
                normal_dist = min(closest_c,q_c)

############# End_Citation [5] #################
            if(normal_dist < circ.radius):
                flag = 1
                break
                # Add logic for calculating new q_new
    return flag


def algo_rrt(q_init, K, D = 100, delta = 2):
    random.seed(None)

    def gen_random_circle():
        x = random.random()*100
        y = random.random()*100
        r = random.randint(3,8)
################ Begin_Citation [6] ###########################
        return Circle((x,y),r, color='black'),x,y
################ End_Citation [6] ##############################

    fig,ax = plt.subplots(figsize=(10,10))

    initial_start = plt.plot([],[],'ro',label = 'Start')
    initial_goal = plt.plot([],[],'go',label = "Goal")
    initial_node = ax.scatter([],[], color='blue', label="Nodes" )
    initial_edge = ax.plot([],[], color='blue', alpha = 0.5, label="Edges")
    initial_path = plt.plot([],[],'yo', label="Path to Goal")   

    plt.legend()

    start = (random.random()*100,random.random()*100)
    end = (random.random()*100, random.random()*100)
    plt.plot(start[0],start[1],'ro')
    plt.plot(end[0],end[1],'go')

    circle_collection = []

    for i in range(0,35):
        circle = gen_random_circle()
        if(math.sqrt((start[0] - circle[1])**2 + (start[1] - circle[2])**2) < circle[0].get_radius()):
            circle = gen_random_circle()
        if(math.sqrt((end[0] - circle[1])**2 + (end[1] - circle[2])**2) < circle[0].get_radius()):
            circle = gen_random_circle()
        else:
            circle_collection.append(circle[0])
            ax.add_patch(circle[0])
    ax.autoscale()
    # plt.show()
    q_init = start # Reassigning q_init a random value
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

        # Add logic to check for collisions
        # flag = 0
        ret_flag = check_collision(q_new,closest_neighbor,circle_collection, dist_min)

        if(ret_flag == 1):
            continue
        
        tree.append(q_new)
        children[q_new] = []
        if closest_neighbor in children.keys():
            children[closest_neighbor].append(q_new)
        
        # Logic for adding goal to the graph
        if(math.sqrt((end[0] - q_new[0])**2 + (end[1]-q_new[1])**2) < 20):
            dist_end = math.sqrt((end[0] - q_new[0])**2 + (end[1]-q_new[1])**2)
            ret_flag = check_collision(end,q_new,circle_collection,dist_end)
            if(ret_flag == 0):
                tree.append(end)
                children[end] = []
                children[q_new].append(end)
                break
            else:
                continue

        t = t + 1
    branches = []
    collection = []
    for key in children.keys():
        branches.append(key)
        
        for val in children[key]:
            branches.append(val)
            
        collection.append(branches)
        branches = []
    
    line_collection = LineCollection(collection)

    # ax.add_collection(line_collection)
    # for i in range(0,len(tree)):
    #     plt.plot(tree[i][0],tree[i][1],'bo')
    plt.plot(end[0],end[1],'go')

    for line in line_collection.get_segments():

        ax.scatter(line[:,0], line[:,1], color='blue' )
        ax.plot(line[:,0], line[:,1], color='blue', alpha = 0.5)
        plt.pause(0.01)
    
    shortest_path = []
    if end in tree:
        end_copy = copy.deepcopy(end)
        while end_copy != start:
            for key,val in children.items():
                if end_copy in val:
                    shortest_path.append(key)
                    end_copy = key
                    break
    
        for i in range(0,len(shortest_path)):
            plt.plot(shortest_path[i][0],shortest_path[i][1],'yo')   
            plt.pause(0.01) 
    plt.plot(start[0],start[1],'ro')        
    plt.show()


algo_rrt((50,50),500)

