#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 02:09:22 2020

@author: alina
"""
#Time comparacy

from HW3_p2 import OrderedList
from HW3_p3 import BST
from HW3_p3 import TreeNode
from random import sample
import matplotlib.pyplot as plt
import statistics
import timeit

lista = OrderedList()
tree = BST()
n = 1000               #Nodes
                        
s = sample(list(range(10*n)),n)
def insertion_lista(s):
    for i in s:
        lista.add(i)
def insertion_tree(s):
    for i in s:
        d = TreeNode(i)
        tree.insert(d)

nodes = sample(list(range(n)),n//10)
    
def search_lista(nodes):
    for i in nodes:
        lista.search(i)
        
def search_tree(nodes):
    for i in nodes:
        tree.search(i)

nodes = sample(s,n//10) #Ensure the nodes are in the list and the tree
def delete_lista(nodes):
    for i in nodes:
        lista.search(i)
        
def delete_tree(nodes):
    for i in nodes:
        tree.delete(i)        
            
def medir_tiempo():
    
    #Declarar listas vacias
    taddlist = []
    tinserttree = []
    tsearchlist = []
    tsearchtree = []
    tdeletelist = []
    tdeletetree = []
    
    #Medir tiempos
    t1 = timeit.Timer("insertion_lista(s)", "from __main__ import insertion_lista,lista,s")
    t1 = t1.timeit(number = 20)   
    t2 = timeit.Timer("insertion_tree(s)", "from __main__ import insertion_tree,tree,s")
    t2 = t2.timeit(number = 20)
    taddlist.append(t1)
    tinserttree.append(t2)
    
    t1 = timeit.Timer("search_lista(nodes)", "from __main__ import search_lista,lista,nodes")
    t1 = t1.timeit(number = 20)   
    t2 = timeit.Timer("search_tree(nodes)", "from __main__ import search_tree,tree,nodes")
    t2 = t2.timeit(number = 20)
    tsearchlist.append(t1)
    tsearchtree.append(t2)
    
    t1 = timeit.Timer("delete_lista(nodes)", "from __main__ import delete_lista,lista,nodes")
    t1 = t1.timeit(number = 20)   
    t2 = timeit.Timer("delete_tree(nodes)", "from __main__ import delete_tree,tree,nodes")
    t2 = t2.timeit(number = 20)
    tdeletelist.append(t1)
    tdeletetree.append(t2)

    # Time means
    taddlist_mean = statistics.mean(taddlist)
    tinserttree_mean = statistics.mean(tinserttree)
    
    tsearchlist_mean = statistics.mean(tsearchlist)
    tsearchtree_mean = statistics.mean(tsearchtree)
    
    tdeletelist_mean = statistics.mean(tdeletelist)
    tdeletetree_mean = statistics.mean(tdeletetree)
    
    #Time rates
    razon_insert = [tinserttree[i]/taddlist[i] for i in range(len(tinserttree))]
    razon_search = [tsearchtree[i]/tsearchlist[i] for i in range(len(tsearchtree))]
    razon_delete = [tdeletetree[i]/tdeletelist[i] for i in range(len(tdeletetree))]
    
    print('taddlist time = ',taddlist_mean,'tinserttree time = ',tinserttree_mean)  
    print('tsearchlist time = ',tsearchlist_mean,'tsearchtree time = ',tsearchtree_mean)  
    print('tdeletelist_sort time = ',tdeletelist_mean,'tdeletetree time = ',tdeletetree_mean)
    

#Results:

     #List                            #Tree
#  Insert  =  27.938 s            Insert =  0.254 s
#  Search  =  13.435 s            Search =  0.010 s
#  Delete  =  13.357 s            Delete =  0.017 s
