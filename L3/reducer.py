#!/usr/bin/env python

import sys

current_cluster = None
points = []
sum_x = 0
sum_y = 0
count = 0

# Number of iterations
num_iterations = 0
#cluster centers
cluster_centers = 0

for line in sys.stdin:
    line = line.strip()
    cluster_id, coordinates = line.split('\t', 1)
    x, y = tuple(map(float, coordinates.split('\t')))
    
    x = float(x)
    y = float(y)
    
    
    if current_cluster == cluster_id:
    
        count += 1
        sum_x += x
        sum_y += y
        
  
    else:
        if count != 0:
     
            # print the average of every cluster to get new centroids
            print(str(sum_x / count) + ", " + str(sum_y / count))
       
        current_cluster = cluster_id
        sum_x = x
        sum_y = y
        count = 1
    print("Cluster data", cluster_id, x, y)

# print last cluster's centroids
if current_cluster == cluster_id and count != 0:
        
        print(str(sum_x / count) + ", " + str(sum_y / count))

            

