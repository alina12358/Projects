#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 15:40:09 2020

@author: alina
"""
def count_currences(lista,element):
    index = Binary_Search(lista, element,0,len(lista))
    counter = 0
    while index is not None:          
          lista.pop(index)
          counter += 1
          index = Binary_Search(lista, element,0,len(lista))
    return print('The searched element appears', counter, 'times in the list')      

def Binary_Search(lista,element,l,r):
    if r >= l:
        n = l + (r - l) // 2
        m = lista[n]
        if m == element:
            return n
        elif m > element:
             return Binary_Search(lista,element,l,n-1)
        else:
            return Binary_Search(lista,element,n+1,r) 
    else: 
        return None
    
#Results:
#        count_currences(A,5) = The searched element appears 0 times in the list
#        count_currences(A,2) = The searched element appears 3 times in the list           
#        count_currences(A,4) = The searched element appears 1 times in the list 

           
def SeqBSearch(lista,element):
    l = 0; r = len(lista)
    while r >= l:
        n = l + (r - l) // 2
        m = lista[n]
        if m == element:
            return n
        elif m > element:
             r = n-1
        else:
            l = n+1
    print('Not in the list')   
    
# Results: 
    #A=[1,1,2,2,2,4,6]
    #SeqBSearch(A,2) = 3
    #SeqBSearch(A,1) = 1
    #SeqBSearch(A,4) = 5
