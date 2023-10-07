from LinkedList import LinkedListSolution,Node
'''
First Approach where a is run n+x+(m+x)
and b is run m+x+(n+x)
'''
def intersection(llA,llB):
    a = llA
    b = llB
    while a!=b:
        if a is None:
            a = llB
        else:
            a=a.next
        if b is None:
            b = llA
        else:
            b = b.next
    return a
'''
Another Approach which list is larger
'''
def intersction(llA,llB):
    if llA.tail is not llB.tail:
        return False
    lenthA = len(llA)
    lenthB = len(llB)

    shorter = llA if lenthA<lenthB else llB
    longer = llB if lenthA<lenthB else llA

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode

#Helper addition Method
def addSameNode(llA,llB,value):
    tempNode = Node(value)
    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


