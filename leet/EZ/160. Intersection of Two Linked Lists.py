class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        sety = set()
        node1= headA
        node2 = headB
        while node1 or node2:
            sety.add(node1)
            node = node.next
        node = headB
        while node:
            if node in sety:
                return node
            node = node.next
        return None
setk = set()
setk.add("kakado")
connation = ListNode(8)
connation.next = ListNode(4)
connation.next.next = ListNode(5)

head1 = ListNode(4)
head1.next = ListNode(1)
head1.next.next = connation

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(1)
head2.next.next.next = connation
print(Solution.getIntersectionNode(Solution,head1,head2))