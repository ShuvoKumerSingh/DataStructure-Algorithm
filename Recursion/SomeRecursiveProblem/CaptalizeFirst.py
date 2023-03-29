'''
Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.
'''
'''
Example

capitalizeFirst(['car', 'taco', 'banana']) # ['Car','Taco','Banana']
'''
# Code Here
def capitalizeFirst(lst):
    new_lst=[]
    if len(lst)<=1:
        new_lst.append(lst[0].capitalize())
    else:
        new_lst.append(lst[0].capitalize())
        new_lst.extend(capitalizeFirst(lst[1:]))
    return new_lst