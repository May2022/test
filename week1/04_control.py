from math import sqrt
def setColours(j):
    if((j%2)==1):  # an odd line. First square black
        oddSquare="black"
        evenSquare="white"
    else:
        oddSquare="white"
        evenSquare="black"
    return(oddSquare,evenSquare)

def writeChessColour():
    for j in range(1,9):   
        oddSquare,evenSquare=setColours(j)
        for i in range(1,9): 
            if((i%2)==1):
                colour=oddSquare
            else:
                colour=evenSquare
            print(i,j,colour)