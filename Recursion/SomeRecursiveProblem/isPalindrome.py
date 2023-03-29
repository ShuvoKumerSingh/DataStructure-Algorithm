'''
Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns false.
'''
'''
Examples

isPalindrome('awesome') # false
isPalindrome('foobar') # false
isPalindrome('tacocat') # true
isPalindrome('amanaplanacanalpanama') # true
isPalindrome('amanaplanacanalpandemonium') # false
'''

def isPalindrome(str):
    if len(str)==0:
        return True
    if str[0]!=str[len(str)-1]:
        return False
    return isPalindrome(str[1:-1])