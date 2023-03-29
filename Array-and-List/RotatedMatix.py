'''
Give an image represented by an N*N matrix write a method to rotate the image by 90 degrees.
Example:
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    output:
    [[7,4,1],[4,5,2],[9,6,3]]
'''
import numpy as np
def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n-layer-1
        for i in range(first,last):
            # Save Top element
            top=matrix[layer][i]
            # move left element to top
            matrix[layer][i]=matrix[-i-1][layer]
            # move bottom element to left
            matrix[-i - 1][layer]=matrix[-layer-1][-i-1]
            # move right element to bottom
            matrix[-layer - 1][-i - 1]=matrix[i][-layer-1]
            # move top element to right
            matrix[i][-layer - 1]=top
    return matrix

