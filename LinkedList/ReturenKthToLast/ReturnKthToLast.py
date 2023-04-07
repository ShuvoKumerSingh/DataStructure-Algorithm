#Time Complexty:-O(n)
#Space Complexity:-O(1)
def nthToLast(ll,n):
    pointe1 = ll.head        #------Time:-O(1)
    pointe2 = ll.head        #------Time:-O(1)

    for i in range(n):       #------Time:-O(n)
        if pointe2 is None:
            return None
        pointe2 = pointe2.next
    while pointe2:       #------Time:-O(n)
        pointe1 = pointe1.next      #------Time:-O(1)
        pointe2 = pointe2.next      #------Time:-O(1)
    return pointe1   #------Time:-O(1)
