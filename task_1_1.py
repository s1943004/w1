""" 
    prerequisite:
    based on Python 3.6
    
    Function:
    ---------
    use nested loop to traverse all the squares of a chessboard from top 
    left to bottom right
    
    Parameters
    ---------
    n: int
        the number of rows or columns of the chessboard
"""


def chessboard(n):
    """
    Loop over all the squares in a chessboard of user-defined size ('n'),
    and print out all the x,y coordinates through nested loop
    """
    for i in range(1,n+1): # the ordinal number of row
        for j in range(1,n+1): # the ordinal number of column
            print(j,i) # print out the x,y coordinates of the square

############################
                        
if __name__ == '__main__':
    """
    Main block
    """
    chessboard(8) # call the looping function, 
                  # set the number of columns or row as parameter of function

