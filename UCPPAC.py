## -*- coding: utf-8 -*-
#"""
#Created on Thu Jan 16 02:02:33 2020
#
#@author: 18moh
#"""
#
#import random
#import numpy as np
#import matplotlib.pyplot as plt
#import math
#import ClusterPAC as cp
#import Storage
#
#
#
#dim=2
#points=200
#cluster=4
#ran=10000
#samplesize=1000
#
#datapoints=cp.generate(points,dim,ran)
#
#sample=[]
#
#for i in range(samplesize):
#    random.shuffle(datapoints)
#    kclust=cp.clustinit(dim,cluster,datapoints)
#    for j in range(30):
#         kclust=cp.kmeans(dim,kclust[0],kclust[1],datapoints)
#    sample.append(kclust)
#    
#
##Reconstruction
#
#ucp=[]
#
#for x in datapoints:
#    for y in datapoints:
#        if(x!=y):
#            ucp.append([x,y,0.0])
#
#for kclust in sample:
#    for i in range(len(kclust[1])):
#        for j in range(len(ucp)):
#            if(ucp[j][0] in kclust[1][i] and ucp[j][1] in kclust[1][i]):
#                ucp[j][2]=ucp[j][2]+1
#
#for i in range(len(ucp)):
#    ucp[i][2]=ucp[i][2]/samplesize
#
#
#Storage.storeData(ucp,'samples')
#print('stored')
#

ucp=Storage.loadData('samples')
reconstruct=[]

error=0.9
errorset=[]
count=0


for x in ucp:
    if(x[2]>error):
        count+=1
        if(x[0] not in errorset):
            errorset.append(x[0])
        if(x[1] not in errorset):
            errorset.append(x[1])
            
print(len(errorset))

cluster1=[]
cluster2=[]
cluster3=[]
cluster4=[]

queue=[]
start=errorset[0]

cluster1.append(start)
queue.append(start)
while(len(queue)>0):
    for rel in ucp:
        if(rel[0]==queue[0] and rel[2]>error):
            if(rel[1] not in cluster1):
                queue.append(rel[1])
                cluster1.append(rel[1])
    del queue[0]

print(len(cluster1))

for x in errorset:
    if(x not in cluster1):
        start=x
        print('nxt')
        break

cluster2.append(start)
queue.append(start)
while(len(queue)>0):
    for rel in ucp:
        if(rel[0]==queue[0] and rel[2]>error):
            if(rel[1] not in cluster2):
                queue.append(rel[1])
                cluster2.append(rel[1])
    del queue[0]
    
print(len(cluster2))

for x in errorset:
    if(x not in cluster1 and x not in cluster2):
        start=x
        print('nxt')
        break

cluster3.append(start)
queue.append(start)
while(len(queue)>0):
    for rel in ucp:
        if(rel[0]==queue[0] and rel[2]>error):
            if(rel[1] not in cluster3):
                queue.append(rel[1])
                cluster3.append(rel[1])
    del queue[0]
    
print(len(cluster3))

for x in errorset:
    if(x not in cluster1 and x not in cluster2 and x not in cluster3):
        start=x
        print('nxt')
        break

cluster4.append(start)
queue.append(start)
while(len(queue)>0):
    for rel in ucp:
        if(rel[0]==queue[0] and rel[2]>error):
            if(rel[1] not in cluster4):
                queue.append(rel[1])
                cluster4.append(rel[1])
    del queue[0]
    
print(len(cluster4))

centroids=[]

for x in cluster4:
    if(x in cluster1 or x in cluster2 or x in cluster3):
        print('common')

centroids=[]

x=0
y=0
for p in cluster1:
    x=x+p[0]
    y=y+p[1]
centroids.append([x/len(cluster1),y/len(cluster1)])
x=0
y=0
for p in cluster2:
    x=x+p[0]
    y=y+p[1]
centroids.append([x/len(cluster2),y/len(cluster2)])
x=0
y=0
for p in cluster3:
    x=x+p[0]
    y=y+p[1]
centroids.append([x/len(cluster3),y/len(cluster3)])
x=0
y=0
for p in cluster4:
    x=x+p[0]
    y=y+p[1]
centroids.append([x/len(cluster4),y/len(cluster4)])

reconstruct=[centroids,[cluster1,cluster2,cluster3,cluster4]]

cp.graphclust(reconstruct)
opt=cp.squarederror(dim,reconstruct[0],reconstruct[1])

print('Cost: ',opt)

#comparison
print()

datapoints=cluster1+cluster2+cluster3+cluster4
errors=[]

for i in range(20):
    random.shuffle(datapoints)
    kclust=cp.clustinit(dim,cluster,datapoints)
    for j in range(20):
         kclust=cp.kmeans(dim,kclust[0],kclust[1],datapoints)
    errors.append(cp.squarederror(dim,kclust[0],kclust[1]))
    
errors.sort()

for i in range(len(errors)):
    if(errors[i]>opt):
        print(i)
        break
    

       

#
#
#
#
#            
#        
#
#
#    
#            
#
#
#    
#
#    
#
#
#
#
#
#
#
#
#
#
#
#
#
