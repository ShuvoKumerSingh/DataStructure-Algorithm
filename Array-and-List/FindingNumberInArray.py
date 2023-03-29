'''
How to check if an array contains a number
example:
arr=[1,2,3,8,10]
number=8
'''
import numpy as np
def findNumber(arr,num):
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1
