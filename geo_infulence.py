import csv
import numpy as np
import heapq
from math import sqrt
import fiona
from shapely.geometry import Point, asShape, shape,Polygon
leaveOut =-1
f_Chicago = fiona.open('shapeFile_Chicago/geo_export_01.shp')
centroids = csv.reader(open('data/centroid_community.csv'), delimiter = ';')

cas = {}

for row in centroids:
         print(row[2])
	 #cas.append({int(row[0]): [row[1], row[2]]})
	 cas[int(row[0])] = [float(row[1]), float(row[2])] 
#creates a object 1: [87.535 , 88.25]
#print(cas)
cSet = list(range(1, 78)) #creates the list from 1 to 77 in a 2d array
if leaveOut > 0:
        cSet.remove(leaveOut)
#print(cSet)

centers = {} 
for i in cSet: #copying one object to other
        centers[i] = cas[i]
#print(centers)

W = np.zeros((len(cSet),len(cSet)))
#creates an array of 77 * 77 with zeros

for i in cSet:
        for j in cSet:
            if i != j:
                if leaveOut < 0:
                    W[i-1][j-1] = 1 / sqrt((1000*(centers[i][0]-centers[j][0]))**2 + (1000*(centers[i][1]-centers[j][1]))**2)
                elif leaveOut > 0:
                    k = i
                    l = j
                    if i > leaveOut:
                        k -= 1
                    if j > leaveOut:
                        l -= 1
                    W[k - 1][l - 1] = 1 / sqrt(
                         (1000 * (centers[i][0] - centers[j][0])) ** 2 + (1000 * (centers[i][1] - centers[j][1])) ** 2)

for i in range(len(cSet)):
        # find largest 6 value
        threshold = heapq.nlargest(6, W[i, :])[-1]
	for j in range(len(cSet)):
            if W[i ][j] < threshold:
                W[i][j] = 0
#print(threshold)
print(W)
