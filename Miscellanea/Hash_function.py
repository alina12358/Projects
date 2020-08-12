#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:42:13 2020

@author: alina
"""
#Function to import text (include everithing in the text, 
#also I didnt knew how to eliminate comas, dots and the other puntuaction signs).
def importtext():        
    from urllib.request import urlopen
    url = "http://www.gutenberg.org/cache/epub/2000/pg2000.txt"
    texto = urlopen(url)
    palabras = []
    for ln in texto:
        palabras.extend(ln.decode("utf-8-sig").split())
    return palabras    

#Main function, it calls the other two to implement the algorithm in the whole text.       
def hashtable():    
    text = importtext()
    m = 2*len(text)
    ht = [None for _ in range(m)] #Hash list
    for s in text:  
        hashed = hashfunc(s,m) 
        if ht[hashed] == s:  #Checking if the word is in this place already, to avoid repeating.
              continue                         
        else:
            ocupado = True
            while ocupado:
                  if ht[hashed] == None: #Check if the place is empty
                     ht[hashed] = s 
                     ocupado = False
                  else:
                      hashed += 1
                      hashed  = hashed % m  #Begin if hashed is grater than m
                      if ht[hashed] == s:   #Check again if the word is in this place to avoid repeating.
                         ocupado = False    # Ending the cycle. 
                         continue
    return ht

#Hash function, as was implemented in the class notes. 
def hashfunc(s,m):
    p = 31
    h = 0
    p_i = 1
    ord_a = ord('a')
    for i in range(len(s)):
        h = (h + (ord(s[i])-ord_a+1)*p_i) % m
        p_i = (p_i * p) % m
    return h % m