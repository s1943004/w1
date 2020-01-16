""" This is the main function.
    prerequisite:
    based on Python 3.6
    
    Function:
    ---------
    use nested loop to traverse all the squares of a chessboard from top 
    left to bottom right; calculate the distance between every 2 squares
    
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
    Loop over all the squares in a chessboard of user-defined size ('n'),
    and calculate the distance between enery 2 squares through nested loop
    --distance between the origin square and the the target square
    """
    for i in range (1,n+1): # the x-coordinate of the origin square 
        for j in range(1,n+1): # the y-coordinate of the origin square 
            for k in range(1,n+1): # the x-coordinate of the target square 
                for m in range(1,n+1): # the y-coordinate of the target square
                    if ((k==i) & (j==m)): # avoid calculating the distance 
                                          # from a square to itself
                        continue
                    else:
                        distance = sqrt((k-i)**2+(j-m)**2)
                        # calculate distance between the origin square 
                        # and the the target square
                        print('{0},{1} to {2},{3} distance {4}'.format(i,j,k,m,distance))
   
############################
                        
if __name__ == '__main__':
    """
    Main block
    """
    distance(8) # call the looping function
