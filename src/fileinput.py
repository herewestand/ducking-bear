'''
Created on Jan 18, 2014

@author: Knightmare
'''

if __name__ == '__main__':
    
    #textfile = open("C:\\Users\\Ivan\\Desktop\\circut.txt","r")
    
    crs = open("C:\\Users\\Ivan\\Desktop\\circut.txt", "r")
    for columns in ( raw.strip().split() for raw in crs ):  
        print (columns[0],columns[1],columns[2],columns[3])
        # a,b,c,d = file.split("    ")
    
    pass