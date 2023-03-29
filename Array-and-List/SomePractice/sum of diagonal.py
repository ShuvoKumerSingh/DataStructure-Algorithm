'''
Given 2D list calculate the sum of diagonal elements.

Example
myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
sumDiagonal(myList2D) # 15

'''

import  numpy as np
def diagonal(lst):
    sum=0
    for i in range(len(lst)):
        sum+=lst[i][i]
    return sum
