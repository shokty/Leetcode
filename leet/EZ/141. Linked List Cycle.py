# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x , next = None):
        self.val = x
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        sety = set()
        while head:
            if head in sety:
                return False
            sety.add(head)
            head = head.next
        return True
head = ListNode(3,ListNode(2))
head.next.next = head
print(Solution.hasCycle(Solution,head))
