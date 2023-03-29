'''
Implement an algorithm to determine if a list has all unique character
'''
def isUnique(lst):
    unique_lst=[]
    for i in lst:
        if i in unique_lst:
            print(i)
            return False
        else:
            unique_lst.append(i)
    return True