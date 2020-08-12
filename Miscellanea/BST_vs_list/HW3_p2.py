#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:29:44 2020

@author: alina
"""
#Some operations in a BST
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.tail = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next    
        
class OrderedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            x = self.head
            xprevious = self.head
            while x != None and item > x.data:
                  xprevious = x
                  x = x.next
                
            if x == None:
               xprevious.set_next(temp)
               self.tail = temp
            elif x == self.head:
                 temp.set_next(x)
                 self.head = temp
            else:    
                 temp.set_next(x)
                 xprevious.set_next(temp)
                
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found
    
    def get_min(self):
        return self.head
    
    def get_max(self):
        return self.tail
        
    def get_k_th(self,k):
        if self.is_empty():
            print('Empty list')
        else:
            x = self.head
            i = 1
            while x!= None and i < k:
                  x = x.next
                  i += 1
            return x
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data()== item:
                found = True                
            else:
                previous = current
                current = current.get_next()
                
        if previous == None:
            self.head = current.get_next()
        elif previous.next == None :
            self.tail = previous
        else:
            previous.set_next(current.get_next())          

    
