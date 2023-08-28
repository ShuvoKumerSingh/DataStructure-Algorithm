# Definition for singly-linked list.
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        preHead = Node(None,None)
        prev = preHead

        while l1 and l2:
            if l1.value<=l2.value:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        return preHead.next




n3 =Node(4,None)
n2 = Node(2,n3)
n1 = Node(1,n2)
l1 = n1

n3 =Node(4,None)
n2 = Node(3,n3)
n1 = Node(1,n2)
l2 = n1
linklist = Solution()

linklist.mergeTwoLists(l1,l2)
print(linklist)

