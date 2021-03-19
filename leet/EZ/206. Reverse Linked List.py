
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None;

        stack = []
        while head != None:
            stack.append(head.val)
            head = head.next

        newhead = ListNode(stack.pop())
        temp = newhead
        while len(stack) >= 1:
            temp.next = ListNode(stack.pop())
            temp = temp.next
        return newhead

head = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
print(Solution.reverseList(Solution,head))