#Time Complexity:- O(n)
#Space Complexity:-O(n)
def removeDuplicates(ll):
    if ll.head is None:      #------Time:-O(1)
        return       #------Time:-O(1)
    else:
        currentNode = ll.head    #------Time:-O(1)
        visitedSet = set([currentNode.value])    #------Time:-O(1)

        while currentNode.next:      #------Time:-O(n)
            if currentNode.next.value in visitedSet:         #------Time:-O(1)
                currentNode.next =  currentNode.next.next        #------Time:-O(1)
            else:        #------Time:-O(1)
                visitedSet.add(currentNode.next.value)       #------Time:-O(1)
                currentNode = currentNode.next       #------Time:-O(1)
        return ll        #------Time:-O(1)

#Time Complexity:- O(n^2)
#Space Complexity:-O(1)
def removeDuplicates1(ll):
    if ll.head is None:      #------Time:-O(1)
        return       #------Time:-O(1)
    currentNode = ll.head        #------Time:-O(1)
    while currentNode:       #------Time:-O(n^2)
        runner = currentNode         #------Time:-O(1)
        while runner.next:       #------Time:-O(n)
            if runner.next.value == currentNode.value:       #------Time:-O(1)
                runner.next = runner.next.next       #------Time:-O(1)
            else:        #------Time:-O(1)
                runner = runner.next         #------Time:-O(1)
        currentNode = currentNode.next       #------Time:-O(1)
    return ll.head       #------Time:-O(1)


