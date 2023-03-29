'''
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]
'''
def middle(lst):
    l,r=0,len(lst)-1
    mid=l+r//2
    return [lst[mid],lst[mid+1]]

#Another Solution:
def middle(lst):
  new=lst[1:]
  del new [-1]
  return new
