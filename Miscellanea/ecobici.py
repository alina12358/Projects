#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:27:28 2020

@author: alina
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Implements a tree, range search and a nearest neighbor to be used with ecobici data. 

# Node class
class kdTree_node:
    def __init__(self, x,y, split_along_x=True):
        self.x = x
        self.y = y
        self.xmax = math.inf
        self.ymax = math.inf
        self.xmin = -math.inf
        self.ymin = -math.inf  
        self.split_along_x = split_along_x
        self.left = None
        self.right = None
        

    def __str__(self):
        return "(x="+str(self.x)+",y="+str(self.y)+")"

# Tree class
class kdTree:
    def __init__(self, xs, ys):
        # Copy the data in sorted arrays (x and y)
        i_x_sort = np.argsort(xs)
        i_y_sort = np.argsort(ys)
        self.root = self.__buildTree(xs,ys,i_x_sort,i_y_sort,True)

        
    def print(self):
        self.__printSubtree(self.root)
    def __printSubtree(self,node):
        if node.left!=None:
            self.__printSubtree(node.left)
            print(node)
            if node.right!=None:
                self.__printSubtree(node.right)
    def __select(self,isorted,isecond):
        iy = np.array([]).astype(int)
        for i in isecond:
            r=(isorted==i)
            if r.any()==True:
                iy=np.append(iy,i)
        return iy
    def __buildTree(self,xs,ys,ix,iy,splitx=None,father=None):
        l= ix.shape[0]
        med = l//2
        # This node corresponds to a split of the data along x axis
        if splitx:
            n= kdTree_node(xs[ix[med]],ys[ix[med]],True)
            if father!=None:
                n.xmin = father.xmin
                n.xmax = father.xmax
                n.ymin = father.ymin
                n.ymax = father.ymax
                if n.y<=father.y:
                    n.ymax = father.y
                else:
                    n.ymin = father.y
            if med>0:       
                sub_iy = self.__select(ix[:med],iy)
                n.left = self.__buildTree(xs,ys,ix[:med],sub_iy,False,n)
            if med+1<l:
                sub_iy = self.__select(ix[med+1:],iy)
                n.right = self.__buildTree(xs,ys,ix[med+1:],sub_iy,False,n)
                # This node corresponds to a split of the data along y
        else: 
            n = kdTree_node(xs[iy[med]],ys[iy[med]],False)
            if father!=None:
                n.xmin = father.xmin
                n.xmax = father.xmax
                n.ymin = father.ymin
                n.ymax = father.ymax
                if n.x<father.x:
                    n.xmax = father.x
                else:
                    n.xmin = father.x
            if med>0:                    
                sub_ix = self.__select(iy[:med],ix)
                n.left = self.__buildTree(xs,ys,sub_ix,iy[:med],True,n)
            if med+1<l:
                sub_ix = self.__select(iy[med+1:],ix)
                n.right = self.__buildTree(xs,ys,sub_ix,iy[med+1:],True,n)
        return n
# Converts lat and lng coordinates to local x,y positions (around the mean)
# This is a first order approximation
def latlngToGlobalXY(coords):
    radius = 6371.0
    dlon = math.pi*(coords[0]-lonMean)/180.0
    dlat = math.pi*(coords[1]-latMean)/180.0
    x = radius*dlon*math.cos(math.pi*latMean/180.0)
    y = radius*dlat
    return x,y

def read_json():
    df_s = pd.read_json('data/estaciones.json', orient='columns')
    # Get positions (longitudes/latitudes)
    stations_positions = df_s[['lon','lat']].values.reshape(-1,2)
    # Average
    global lonMean, latMean    
    lonMean = np.average(stations_positions[:,0])
    latMean = np.average(stations_positions[:,1])
    # Converts into x,y around the average
    locs_bici = np.apply_along_axis(latlngToGlobalXY, 1, stations_positions)
    # Plot the station positions and the number of slots
    plt.scatter(locs_bici[:,0],locs_bici[:,1])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend('Ecobici stations')
    plt.show()
    return locs_bici
def drawSubtree(node,s):
    if node.left!=None:
        drawSubtree(node.left,s+1)
    # Draw the current node as a line segment
    width = 8-s
    if node.split_along_x==True:
        if (width>0):
            plt.plot([node.x,node.x],[max(-5,node.ymin),min(node.ymax,5)],linewidth=width)
    else:
        if (width>0):
            plt.plot([max(-5,node.xmin),min(node.xmax,5)],[node.y,node.y],linewidth=width)
    if node.right!=None:
        drawSubtree(node.right,s+1)
def draw(kdTree):
    drawSubtree(kdTree.root,0)
    plt.show()
   

def range_search(x0,y0,xf,yf,tree):
    return finding(x0,y0,xf,yf,tree.root,[])
    

def finding(x0,y0,xf,yf,node, lista):
    if x0 < node.x and node.x < xf and y0 < node.y and node.y < yf: 
       lista.append((node.x,node.y))  
    if node.left:
        if intersect(x0,y0,xf,yf,node.left):
           lista = finding(x0,y0,xf,yf,node.left,lista)
    if node.right:
        if intersect(x0,y0,xf,yf,node.right):
           lista = finding(x0,y0,xf,yf,node.right,lista)
    return lista


def intersect(x0,y0,xf,yf,node): 
    intersection = True
    if node.xmax < x0 or node.xmin > xf or node.ymax < y0 or node.ymin > yf:
        intersection = False
    return intersection        
        

class kdTree_var:
    def __init__(self, xs, ys):
        # Copy the data in sorted arrays (x and y)
        i_x_sort = np.argsort(xs)
        i_y_sort = np.argsort(ys)
        self.root = self.__buildTree(xs,ys,i_x_sort,i_y_sort)
    def print(self):
        self.__printSubtree(self.root)
    def __printSubtree(self,node):
        if node.left!=None:
            self.__printSubtree(node.left)
            print(node)
            if node.right!=None:
                self.__printSubtree(node.right)
    def __select(self,isorted,isecond):
        iy = np.array([]).astype(int)
        for i in isecond:
            r=(isorted==i)
            if r.any()==True:
                iy=np.append(iy,i)
        return iy
    def __buildTree(self,xs,ys,ix,iy,father=None):
        l= ix.shape[0]
        med = l//2
        mediax = sum(xs[x] for x in ix)/len(ix)
        mediay = sum(ys[y] for y in iy)/len(iy)
        varx = sum((xs[x]-mediax)**2 for x in ix)/len(ix)
        vary = sum((ys[y]-mediay)**2 for y in iy)/len(iy) 
        splitx = (varx > vary)     
        # This node corresponds to a split of the data along x axis
        if splitx:
            n= kdTree_node(xs[ix[med]],ys[ix[med]],splitx)
            if father!=None:
                n.xmin = father.xmin
                n.xmax = father.xmax
                n.ymin = father.ymin
                n.ymax = father.ymax
                if n.y<=father.y:
                    n.ymax = father.y
                else:
                    n.ymin = father.y
            if med>0:       
                sub_iy = self.__select(ix[:med],iy)
                n.left = self.__buildTree(xs,ys,ix[:med],sub_iy,n)
            if med+1<l:
                sub_iy = self.__select(ix[med+1:],iy)
                n.right = self.__buildTree(xs,ys,ix[med+1:],sub_iy,n)
                # This node corresponds to a split of the data along y
        else: 
            n = kdTree_node(xs[iy[med]],ys[iy[med]],splitx)
            if father!=None:
                n.xmin = father.xmin
                n.xmax = father.xmax
                n.ymin = father.ymin
                n.ymax = father.ymax
                if n.x<father.x:
                    n.xmax = father.x
                else:
                    n.xmin = father.x
            if med>0:                    
                sub_ix = self.__select(iy[:med],ix)
                n.left = self.__buildTree(xs,ys,sub_ix,iy[:med],n)
            if med+1<l:
                sub_ix = self.__select(iy[med+1:],ix)
                n.right = self.__buildTree(xs,ys,sub_ix,iy[med+1:],n)
        return n

        
   
def explore(query,node,closest):
     p = np.array([node.x,node.y])
     if distance(query - p) < distance(query - closest):
        closest = p
     if node.left:
        dx = max(node.left.xmin - query[0],0,query[0] - node.left.xmax)
        dy = max(node.left.ymin - query[1],0,query[1] - node.left.ymax)
        d = np.array([dx,dy])
        if distance(d) < distance(query - closest):
           closest = explore(query,node.left,closest)
     if node.right:
        dx = max(node.right.xmin - query[0],0,query[0] - node.right.xmax)
        dy = max(node.right.ymin - query[1],0,query[1] - node.right.ymax)
        d = np.array([dx,dy])
        if distance(d) < distance(query - closest):
           closest = explore(query,node.right,closest)
     return closest
 
def nearest_neighbor(x,y,tree):
    query = np.array([x,y])
    global closest,distance
    closest = np.array([tree.root.x,tree.root.y])
    distance = np.linalg.norm 
    return explore(query,tree.root,closest)       
