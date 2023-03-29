def findMissingValue(lst,n):
    sum1 = n*(n+1)/2
    sum2 = sum(lst)
    return sum1-sum2

lst=[1,2,3,4,6,7,8,9,10]
print(findMissingValue(lst,10))