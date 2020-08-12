#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 16:06:31 2020

@author: alina
"""

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


def postoinfix(expression):
    number_stack = Stack()
    ops = {"+": (lambda x,y: x+y), "-": (lambda x,y: x-y),"*": (lambda x,y: x*y),"/": (lambda x,y: x/y)}    
    
    for x in expression:
        if x == "+" or x == "-" or x == "*" or x == "/":
           number_stack.push(ops[x](int(number_stack.pop()),int(number_stack.pop())))       
        elif x == ' ':
            continue
        else:  
             number_stack.push(x)
    return number_stack.pop()    
             