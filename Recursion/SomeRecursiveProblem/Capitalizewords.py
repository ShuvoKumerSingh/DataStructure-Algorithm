'''
Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word capitalized.
'''
'''
Examples

words = ['i', 'am', 'learning', 'recursion']
capitalizeWords(words) # ['I', 'AM', 'LEARNING', 'RECURSION']
'''
#Code
def capitalizeWords(lst):
    result=[]

    if len(lst)==0:
        return result
    result.append(lst[0][0:].upper())
    return result + capitalizeWords(lst[1:])