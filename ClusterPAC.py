# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 02:28:09 2020

@author: 18moh
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import math

#Data Generation Algorithms
def generate(num,dim,ran):
    random.seed(5)
    points=[]
    for i in range(num):
        p=[]
        for j in range(dim):
            p.append(random.randint(-ran,ran))
        points.append(p)
    return points

def generatecluster2d(num,ran1,ran2,ran3,ran4):
    random.seed(0)
    points=[]
    x=[]
    y=[]
    for j in range(math.ceil(num)):    
        x.append(random.randint(ran1,ran2))
        y.append(random.randint(ran3,ran4))
    points.append(x)
    points.append(y)
    return points


#K-means Algorithm
def distance(p1,p2,dim):
    raw=[]
    for i in range(dim):
        raw.append(p1[i]-p2[i])
    dist=0
    for x in raw:
        dist=dist+x**2
    return dist**0.5

def clustinit(dim,clustnum,points):
    centroids=[]
    clusters=[]
    for i in range(clustnum):
        centroids.append(points[i])
        clusters.append([])
    for x in points:
        dist=[]
        for j in range(len(centroids)):
            dist.append(distance(x,centroids[j],dim))
        mindist=dist[0]
        minclust=0
        for i in range(len(dist)):
            if(dist[i]<mindist):
                mindist=dist[i]
                minclust=i
        clusters[minclust].append(x)
    return [centroids,clusters]

def specclustinit(dim,clustnum,points,val):
    centroids=[]
    clusters=[]
    for x in val:
        centroids.append(points[x])
    for x in points:
        dist=[]
        for j in range(len(centroids)):
            dist.append(distance(x,centroids[j],dim))
        mindist=dist[0]
        minclust=0
        for i in range(len(dist)):
            if(dist[i]<mindist):
                mindist=dist[i]
                minclust=i
        clusters[minclust].append(x)
    return [centroids,clusters]

def graphclust(kclust):
    for i in range(len(kclust[1])):
        xs = [x[0] for x in kclust[1][i]]
        ys = [x[1] for x in kclust[1][i]]
        plt.scatter(xs, ys)
    xs = [x[0] for x in kclust[0]]
    ys = [x[1] for x in kclust[0]]
    plt.scatter(xs, ys, marker='X', s=200)
    plt.show()
    plt.close()
    
def kmeans(dim,centroids,clusters,points):
    newcentroids=[]
    for i in range(len(clusters)):
        point=[]
        for j in range(dim):
            x=0
            for k in clusters[i]:
                x=x+k[j]
            x=x/len(clusters[i])
            point.append(x)
        newcentroids.append(point)
    newclusters=[]
    for i in range(len(clusters)):
        newclusters.append([])
    for x in points:
        dist=[]
        for j in range(len(newcentroids)):
            dist.append(distance(x,newcentroids[j],dim))
        mindist=dist[0]
        minclust=0
        for i in range(len(dist)):
            if(dist[i]<mindist):
                mindist=dist[i]
                minclust=i
        newclusters[minclust].append(x)
    return [newcentroids,newclusters]
        
def squarederror(dim,centroids,clusters):
    error=0
    for i in range(len(clusters)):
        clusterror=0
        for x in clusters[i]:
            clusterror=clusterror+distance(x,centroids[i],dim)**2
        error=error+clusterror
    return error

def inertia(dim,centroids,clusters):
    pass


#Data Generation Parametres
#dim=2
#cluster=4
#width=0
#points=1000
#drange=10000
#
#cluster1=generatecluster2d(points/cluster,-drange,-drange*width,-drange,-drange*width)
#cluster2=generatecluster2d(points/cluster,drange*width,drange,-drange,-drange*width)
#cluster3=generatecluster2d(points/cluster,-drange,-drange*width,drange*width,drange)
#cluster4=generatecluster2d(points/cluster,drange*width,drange,drange*width,drange)
#
#plt.scatter(cluster1[0],cluster1[1])
#plt.scatter(cluster2[0],cluster2[1])
#plt.scatter(cluster3[0],cluster3[1])
#plt.scatter(cluster4[0],cluster4[1])
#plt.show()
#plt.close()
#
#datapoints=[]
#x=(cluster1[0]+cluster2[0]+cluster3[0]+cluster4[0])
#y=(cluster1[1]+cluster2[1]+cluster3[1]+cluster4[1])
#for i in x:
#    datapoints.append([i]) 
#for i in range(len(datapoints)):
#    datapoints[i].append(y[i])

#xs = [x[0] for x in datapoints]
#ys = [x[1] for x in datapoints]
#plt.scatter(xs, ys)
#plt.show
#plt.close


#Execute Program

#
#dim=3
#cluster=4
#
#datapoints=generate(200,dim,1000)
#
#
#costs=[]
#centroids=[]
#
#for i in range(400):
#    random.shuffle(datapoints)
#    kclust=clustinit(dim,cluster,datapoints)
#    for j in range(30):
#         kclust=kmeans(dim,kclust[0],kclust[1],datapoints)
#    costs.append(squarederror(dim,kclust[0],kclust[1]))
#    centroids.append(kclust[0])
#    #graphclust(kclust)
#
#minimum=costs[0]
#for x in costs:
#    if(x<minimum):
#        minimum=x
#        
#print(minimum)
#
#for i in range(len(costs)):
#    costs[i]=costs[i]-minimum
#    
#
#mincost=costs[0]
#newset=[]
#for i in range(len(costs)):
#    newset.append([i])
#    if(mincost>costs[i]):
#        mincost=costs[i]
#    newset[i].append(mincost)
#
#xs = [x[0] for x in newset]
#ys = [x[1] for x in newset]
#plt.xlim(0, len(newset))
#plt.ylim(0, max(costs))
#plt.scatter(xs, ys)
#plt.show()
#plt.close()
#    
#
#plt.hist(costs, bins=100)
#plt.ylabel('Probability')
#plt.show()
#
#
#
#
#
#
#





