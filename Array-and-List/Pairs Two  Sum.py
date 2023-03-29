'''
Write a program to find all pais of integers whose sum is equal to a given number.
example:lst=[2,6,3,9,11],target=9,output=[1,2]
'''
#Code
def findPairs(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                continue
            if nums[i]+nums[j]==target:
                return [i,j]

              #Another is using Two pointer
def findPairs(nums,target):
    left,right=0,len(nums)-1
    while left<=right:
        current_sum = nums[left]+nums[right]
        if current_sum>target:
            right-=1
        elif current_sum<target:
            left+=1
        else:
            return [left,right]

