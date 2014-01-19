'''
Created on Jan 15, 2014

@author: Knightmare
'''
from circuit import NAND
from circuit import AND
from circuit import OR
from circuit import XOR
from circuit import XNOR
from circuit import NOR 

if __name__ == '__main__':
    p=NAND(input1=1,input2=1)
    x=AND(input1=p.getNANDcarry(), input2=1)
    print(x.getANDcarry())
    pass