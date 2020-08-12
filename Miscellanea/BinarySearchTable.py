    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
"""    Created on Sat Mar 14 17:21:33 2020
    
    @author: alina
    """

class BinarySearchTable:
# Constructor
    def __init__(self):
        self.size = 0
        self.keys = []
        self.data = []    
# Search a key and returns its position (-1 if not found)
        
    def put(self, key, data):
        pos = self.__binary_search(0,self.len()-1,key)
        if pos<0:
            self.keys.append(key)
            self.data.append(data)
            self.size = self.size + 1
        else:
            self.data[pos] = data
                
    def get(self, key):
        pos = self.__binary_search(0,self.size-1,key)
        if pos>=0:
            return self.data[pos]
        return None            
    
    def len(self):
        return self.size
    
    def __delitem__(self, key):
        pos = self.__binary_search(0,self.len()-1,key)
        if pos>=0:
            del self.keys[pos]
            del self.data[pos]
            self.size = self.size - 1
    
    def __binary_search(self,imin,imax,key):
        if imax >= imin:
# Terminal case 1
            if key<self.keys[imin]:
                return -1
# Recursion
            median = (imin+imax+1)// 2
            if self.keys[median]==key:
                return median
            else:
                if self.keys[median]<key:
                    return self.__binary_search(median+1, imax, key)
                else:
                    return self.__binary_search(imin,median-1, key)
        else:
            return -1
# Operator in
    def __contains__(self, key):
        pos = self.__binary_search(0,len(self.keys),key)
        if pos>=0:
            return True
        return False
    
    def __str__(self):
        return ' '.join("("+str(k)+","+str(d)+")" for k,d in zip(self.keys,self.data))
    
    
    
#table = BinarySearchTable()
#table.put(1,"Ain")
#table.put(33,"Gironde")
#table.put(64,"Pyrenees Atlantique")
#table.put(64,"PyrÃ©nÃ©es-Atlantique")
#print(table.len())
#print(table.get(33))
#print(table.get(34))
#print(35 in table)
#print(64 in table)
#print(table)
#del table[33]
#print(table)
#print(table.len())
#            
#3
#Gironde
#None
#False
#True
#(1,Ain) (33,Gironde) (64,PyrÃ©nÃ©es-Atlantique)
#(1,Ain) (64,PyrÃ©nÃ©es-Atlantique)
#2    