'''
Given a list, write a function to get first, second best scores from the list.
List may contain duplicates.
Example
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
firstSecond(myList) # 90 87
'''
def firstSecond(myList):
    value=2
    new_lst = []
    while value!=0:
        lst_max = max(myList)
        new_lst.append(lst_max)
        myList.remove(lst_max)
        value-=1
    return new_lst[0],new_lst[1]
res=firstSecond(myList)

#Another Solution
def firstSecond(given_list):
 
    a = given_list   #make a copy
 
    a.sort(reverse=True)
 
    print(a)
 
    first = a[0]
 
    second = None
 
    for element in given_list:
 
        if element != first:
 
            second = element
 
            return first, second
