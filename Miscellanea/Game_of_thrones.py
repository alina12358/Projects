#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:14:53 2020

@author: alina
"""
import csv 
import math

#Count the connected components and tells if a person is connected with another in a Game of Thrones based graph.
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.mark = 0
        self.distance = 0
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    def mark(self):
        return self.mark
    
    def dist(self):
        return self.distance

class Queue:
    def __init__(self):
            self.items = []
    
    def is_empty(self):
       return self.items == []

    def enqueue(self, item):
       self.items.append(item)
    
    def dequeue(self):
       return self.items.pop(0)
        
class Stack:
    def __init__(self):
       self.items = []
    
    def is_empty(self):
       return self.items == []

    def push(self, item):
       self.items.append(item)
    
    def pop(self):
       return self.items.pop()

    def peek(self):
       return self.items[len(self.items)-1]

    def size(self):
       return len(self.items)
   
        
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)
        
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
        
    def DFS_visit(self,s):
        S = Stack()
        S.push(s)
        size = 0
        while not S.is_empty():
            v = S.pop()
            if v.mark != 1:
                v.mark = 1
                size += 1
                for w in v.getConnections():
                    S.push(w) 
        return size                   
                    
# Depth-first search, returns the size and the number of connected components  
    def DFS(self):
        connected = 0
        sizelist = []
        for vertice in self:
            vertice.mark = 0
            
        for vertice in self:
            if vertice.mark != 1:
               size = self.DFS_visit(vertice)
               sizelist.append(size) 
               connected += 1
        return sizelist,connected       
#G.DFS() = ([274, 2], 2)
           
#  Breadth-First-Search, returns the dstance between nodes with keys 'name1' and 'name2'                
    def BFS(self,name1,name2):
        s = self.getVertex(name1)
        t = self.getVertex(name2)
        for vertice in self:
            if vertice != s:
               vertice.mark = 'white'
               vertice.distance = math.inf
        s.mark = 'gray'       
        s.distance = 0
        Q = Queue()
        Q.enqueue(s)
        while not Q.is_empty():
            u = Q.dequeue()
            for v in u.getConnections():
                if v.mark == 'white':
                   v.mark = 'gray'
                   v.distance = u.distance + 1
                   Q.enqueue(v)
                if v == t:
                   return v.distance                   
            u.mark = 'black'  
        return t.distance
        
## G.BFS('Sansa-Stark','Arya-Stark') = 1
# G.BFS('Brynden-Tully','Balon-Greyjoy') = 4
# G.BFS('Elia-Martell','Brienne-of-Tarth') = 2   
# G.BFS('Joaquin-Penia','Brienne-of-Tarth') = inf        

def ImportCSV():
    skipfirstline = True
    Grafo = Graph()
    with open('ASOIAF_edges.csv') as csvedges:
        conexiones = csv.reader(csvedges, delimiter=',')    
        for edge in conexiones:
            if not skipfirstline:
               Grafo.addEdge(edge[0],edge[1],edge[3])
            skipfirstline = False    
    return Grafo       
    

    
