'''
Duplicate Number
Write a function to find the duplicate number on given integer array/list.

Example

removeDuplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
'''
def removeDuplicates(myList):
    new_lst=[]
    for ele in myList:
        if ele not in new_lst:
            new_lst.append(ele)
        else:
            pass
    return new_lst
