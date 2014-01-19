'''
Created on Jan 9, 2014

@author: Knightmare
'''


class NAND():
    def __init__(self , input1, input2, carry1=0, carry2=1):
        self.__input1 = input1
        self.__input2 = input2
        self.__carry1 = carry1
        self.__carry2 = carry2
        
        
    def getNANDcarry(self):
        if  self.__input1 == 0  & self.__input2 == 0:
            return self.__carry2
        elif  self.__input1 == 1 & self.__input2 == 0:
            return self.__carry2
        elif  self.__input1 == 0 & self.__input2 == 1:
            return self.__carry2
        elif  self.__input1 == 1 & self.__input2 == 1:
            return self.__carry1
        else: 
            return "not  0 or 1"  
class AND():
    def __init__(self , input1, input2, carry1=0, carry2=1):
        self.__input1 = input1
        self.__input2 = input2
        self.__carry1 = carry1
        self.__carry2 = carry2
        
        
    def getANDcarry(self):
        if  self.__input1 == 0  & self.__input2 == 0:
            return self.__carry1
        elif  self.__input1 == 1 & self.__input2 == 0:
            return self.__carry1
        elif  self.__input1 == 0 & self.__input2 == 1:
            return self.__carry1
        elif  self.__input1 == 1 & self.__input2 == 1:
            return self.__carry2
        else: 
            return "not  0 or 1"      
class OR():
    def __init__(self , input1, input2, carry1=0, carry2=1):
        self.__input1 = input1
        self.__input2 = input2
        self.__carry1 = carry1
        self.__carry2 = carry2
        
        
    def getORcarry(self):
        if  self.__input1 == 0  & self.__input2 == 0:
            return self.__carry1
        elif  self.__input1 == 1 & self.__input2 == 0:
            return self.__carry2
        elif  self.__input1 == 0 & self.__input2 == 1:
            return self.__carry2
        elif  self.__input1 == 1 & self.__input2 == 1:
            return self.__carry2
        else: 
            return "not  0 or 1"      
class XOR():
    def __init__(self , input1, input2, carry1=0, carry2=1):
        self.__input1 = input1
        self.__input2 = input2
        self.__carry1 = carry1
        self.__carry2 = carry2
        
        
    def getXORcarry(self):
        if  self.__input1 == 0  & self.__input2 == 0:
            return self.__carry1
        elif  self.__input1 == 1 & self.__input2 == 0:
            return self.__carry2
        elif  self.__input1 == 0 & self.__input2 == 1:
            return self.__carry2
        elif  self.__input1 == 1 & self.__input2 == 1:
            return self.__carry1
        else: 
            return "not  0 or 1"
class NOR():
    def __init__(self , input1, input2, carry1=0, carry2=1):
        self.__input1 = input1
        self.__input2 = input2
        self.__carry1 = carry1
        self.__carry2 = carry2
        
        
    def getNANDcarry(self):
        if  self.__input1 == 0  & self.__input2 == 0:
            return self.__carry2
        elif  self.__input1 == 1 & self.__input2 == 0:
            return self.__carry1
        elif  self.__input1 == 0 & self.__input2 == 1:
            return self.__carry1
        elif  self.__input1 == 1 & self.__input2 == 1:
            return self.__carry1
        else: 
            return "not  0 or 1"                
class XNOR():
    def __init__(self , input1, input2, carry1=0, carry2=1):
        self.__input1 = input1
        self.__input2 = input2
        self.__carry1 = carry1
        self.__carry2 = carry2
        
        
    def getNANDcarry(self):
        if  self.__input1 == 0  & self.__input2 == 0:
            return self.__carry2
        elif  self.__input1 == 1 & self.__input2 == 0:
            return self.__carry1
        elif  self.__input1 == 0 & self.__input2 == 1:
            return self.__carry1
        elif  self.__input1 == 1 & self.__input2 == 1:
            return self.__carry2
        else: 
            return "not  0 or 1"          
    
       
        
        



        