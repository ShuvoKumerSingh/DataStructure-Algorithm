class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
  def reverse(self):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            temp=current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp
        self.head,self.tail = self.tail,self.head
        return self.__str__()







revers=LinkedList()
revers.append(1)
revers.append(2)
revers.append(3)
revers.append(4)
revers.append(5)
print(revers)
print(revers.reverse())
