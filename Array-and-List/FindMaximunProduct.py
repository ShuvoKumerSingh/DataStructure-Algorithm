'''
How to find maximun product of two integers in the array where all elements are positive
Example:
    array = np.array([1,2,10,27,97,8,1,4,6,3])

'''

import numpy as np
def findMaxProduct(arr):
    max_product=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if max_product<arr[i]*arr[j]:
                max_product=arr[i]*arr[j]
    return max_product
