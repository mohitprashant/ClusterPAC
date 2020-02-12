# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:04:53 2020

@author: 18moh
"""

import Storage as st
import ClusterPAC as cp
import random
import math
import matplotlib.pyplot as plt

points=200
dim=2
ran=10000
samplesize=20
cluster=4

datapoints=cp.generate(points,dim,ran)

sample=[]

for i in range(samplesize):
    random.shuffle(datapoints)
    kclust=cp.clustinit(dim,cluster,datapoints)
    for j in range(5):
         kclust=cp.kmeans(dim,kclust[0],kclust[1],datapoints)
    sample.append(kclust)
    cp.graphclust(kclust)
    print('Cost: ',cp.squarederror(dim,kclust[0],kclust[1]))
    print('Sample size: 1000     Error threshold: 0.8')
    print('K-Means iterations: 15')

for kclust in sample:
    print(cp.squarederror(dim,kclust[0],kclust[1]))
    


