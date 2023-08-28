class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result += str(temp.value)
            if temp.next is not None:
                result+='->'
            temp = temp.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is  not None:
            slow = slow.next
            fast = fast.next.next
        return  slow.value















revers=LinkedList()
revers.append(1)
revers.append(2)
revers.append(3)
revers.append(4)
revers.append(5)
# revers.append(6)

print(revers)
print(revers.find_middle())

