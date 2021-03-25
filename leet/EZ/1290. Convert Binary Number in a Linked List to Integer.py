# Definition for singly-linked list.
from urllib3.connectionpool import xrange


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        number = 0
        stack.reverse()
        for i in range(len(stack)):
            number +=  stack[i] * (pow(2,i))
        return number

print(Solution.getDecimalValue(Solution,ListNode(1,ListNode(0,ListNode(1)))))