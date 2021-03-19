import queue
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        Q = queue.Queue()
        def helper(node):
            if node != None:
                Q.put(node.val)
            helper(Q.left)
            helper(Q.right)
        newroot = TreeNode(Q.get())
        temp = newroot
        helper(root)
        while Q:
            temp.right = TreeNode(Q.get())
            temp = temp.right
        return newroot