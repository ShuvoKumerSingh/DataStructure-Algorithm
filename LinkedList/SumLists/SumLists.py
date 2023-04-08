from LinkedList import LinkedListSolution
def sumList(llA,llB):
    n1 = llA.head
    n2 = llB.head
    carray = 0
    ll = LinkedListSolution()

    while n1 or n2:
        result = carray
        if n1:
            result+=n1.value
            n1 = n1.next

        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result%10))
        carray = int(result/10)
    return ll

