# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        answear = []
        while l1 and l2:
            if (l1.val < l2.val):
                answear.append(l1.val)
                l1 = l1.next
            else:
                answear.append(l2.val)
                l2 = l2.next
        while l2:
            answear.append(l2.val)
            l2 = l2.next
        while l1:
            answear.append(l1.val)
            l1.next
        if len(answear) < 1:
            return None
        listy = temp = ListNode(answear[0])
        for i in range(1,len(answear)):
            temp.next = ListNode(answear[i])
            temp = temp.next
        return listy
