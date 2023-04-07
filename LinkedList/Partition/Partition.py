#Time Complexty:-O(n)
#Space Complexity:-O(1)
def partition(ll,x):
    currentNode = ll.head       #------Time:-O(1)
    ll.tail = ll.head       #------Time:-O(1)

    while currentNode:  #------Time:-O(n)
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value<x:
            currentNode.next = ll.head  #------Time:-O(1)
            ll.head = currentNode
        else:
            ll.tail.next = currentNode  #------Time:-O(1)
            ll.tail = currentNode
        currentNode = nextNode
    if ll.tail.next is not None:    #------Time:-O(1)
        ll.tail.next = None
    return ll
