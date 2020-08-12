#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:00:41 2020

@author: alina
"""

# Python program to demonstrate insert operation in binary search tree  
  
# A utility class that represents an individual TreeNode in a BST 
class TreeNode: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
        self.parent = None

# A utility function to insert a new TreeNode with the given key 
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,node): 
        if self.root is None: 
            self.root = node 
        else:
            self.add(self.root,node)
            
    def add(self,root,node):    
        if root.val < node.val: 
           if root.right is None: 
              root.right = node 
              node.parent = root
           
           else: 
               self.add(root.right, node) 
                
        else: 
            if root.left is None: 
                root.left = node 
                node.parent = root
            else: 
                self.add(root.left, node) 
                        
        
    def search(self,key):
        if self.root == None:
            return None
        else:
            return self.tsearch(self.root,key)
            
    def tsearch(self,x,k):
        if x == None or k == x.val:
            return x
        if k < x.val:
            return self.tsearch(x.left,k)
        else:
            return self.tsearch(x.right,k)
    
    def minim(self,root):
        while root.left != None:
            root = root.left
        return root
    
    def maxim(self):
        x = self.root
        while x.right != None:
            x = x.right
        return x
        
    # A utility function to do inorder tree traversal 
    def get_kth(self,k):
        counter = 1
        x = self.minim(self.root)
        while counter < k :
            x = self.sucesor(x)
            counter += 1
        return x    
            
    def sucesor(self,node):
         if node.right !=  None:
             return self.minim(node.right)
         else:
             padre = node.parent
             while padre != None and node == padre.right:
                 node = padre
                 padre = padre.parent
             return padre    
             
    def delete(self,keynode):
        node = self.search(keynode)
        if node is None:
            print('The value is not in the tree')
        else:
            if node.left == None or node.right == None:
                y = node  
            else: 
                y = self.sucesor(node)
            if y.left != None:
                x = y.left                
            else: 
                x = y.right
            if x != None:
                x.parent = y.parent
            if y.parent == None:
                x = self.root
            else:
                if y == y.parent.left:
                   y.parent.left = x
                else: 
                   y.parent.right = x
            if y != node:
                node.val = y.val
            return y    
        
from random import sample
def construct(n,k):    
    tree = BST()
    for i in sample(range(1,n+1),k):
        tree.insert(TreeNode(i))
    return tree
    
    
    
    
