'''
Write a function to find the missing number in a given integer array of 1 to 100.
Example
missingNumber([1, 2, 3, 4, 6], 6) # 5
'''
def missingNumber(myList,totalCount):
    sum1 = totalCount*(totalCount+1)/2
    sum2 = sum(myList)
    get_missing_num = sum1-sum2
    return get_missing_num

#Another Solution
def missingNumber(myList, totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)
    actualSum = 0
    for i in myList:
        actualSum += i
    return int(expectedSum - actualSum)
