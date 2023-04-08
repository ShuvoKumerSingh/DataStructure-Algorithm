from LinkedList import LinkedListSolution,Node
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


