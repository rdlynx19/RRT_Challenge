# Rapidly Exploring Random Trees
Rapidly exploring random trees (RRT) is a path planning algorithm originally published in 1998 by Steven M. LaValle.

This repository contains an implementation of the RRT algorithm both in an obstacle-free environment and an obstacle-filled environment. 

## RRT Algorithm
The pseudo code of the RRT algorithm can be described as shown in this picture:
![image](/images/rrt-algorithm.png)
    
## Results
In an obstacle-free environment, 500 iterations of RRT give almost uniform coverage throughout the space.
![image](/images/basic-rrt.png)

In the obstacle-filled environment, the RRT algorithm is used to find the path from a start position to a goal position. The shortest path from the start to goal is indicated in yellow.
![image](/images/collision-rrt.png)

## Reference
This implementation was a part of the NU MSR hackathon. More details can be found here: https://nu-msr.github.io/hackathon/rrt_challenge.html