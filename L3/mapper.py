#!/usr/bin/env python

import sys
from math import sqrt

# Function to calculate the distance between two points
def euclidean_distance(point1, point2):
    return sum((x - y) ** 2 for x, y in zip(point1, point2)) ** 0.5
    



def mapper():
    centroids = []
    for line in sys.stdin:
        line = line.strip()
        coordinates = line.split()
        # print ('%s' % (coordinates))
        point = tuple(map(float, coordinates))
        #  print('%d', point)

        if not centroids:
            centroids = [point]
        elif len(centroids) < 3:
            centroids.append(point)
        
        
        #  print("Centroid")
        #   print('%d', centroids)
        nearest_centroid_id = None
        min_distance = float('inf')

        for centroid_id, centroid in enumerate(centroids):
            distance = euclidean_distance(point, centroid)
            if distance < min_distance:
                min_distance = distance
                nearest_centroid_id = centroid_id

        print('%d\t%s' % (nearest_centroid_id, '\t'.join(coordinates)))

if __name__ == "__main__":
 
    mapper()