'''
Write a recursive function called reverse which accepts a string and returns a new string in reverse.
Examples:
reverse('python') # 'nohtyp'
reverse('appmillers') # 'srellimppa'
'''
def reverse(str):
    if len(str)<=1:
        return str
    return str[-1]+reverse(str[:-1])