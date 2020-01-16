""" This is the main function.
    prerequisite:
    based on Python 3.6
    
    Parameters
    ---------
    n: int
        the number of rows or columns of the chessboard
"""


############################
from math import sqrt

############################

def distance(n):
    """

    """
    for i in range (1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                for m in range(1,n+1):
                    if ((k==i) & (j==m)): #avoid calculating the distance from a square to itself
                        continue
                    else:
                        distance = sqrt((k-i)**2+(j-m)**2)
                        print('{0},{1} to {2},{3} distance {4}'.format(i,j,k,m,distance))
   
############################
                        
if __name__ == '__main__':
    """
    Main block
    """
    distance(8) #call the looping function
