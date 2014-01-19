'''
Created on Jan 18, 2014

@author: Knightmare
'''

if __name__ == '__main__':
    
    #textfile = open("C:\\Users\\Ivan\\Desktop\\circut.txt","r")
    
    crs = open("C:\\Users\\Ivan\\Desktop\\circut.txt", "r")
    for rows in ( raw.strip().split() for raw in crs ):  
        print (rows[0],rows[1],rows[2],rows[3])
        # a,b,c,d = file.split("    ")
    
    pass