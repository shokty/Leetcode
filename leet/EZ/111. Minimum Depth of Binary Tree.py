# Definition for a binary tree node.

import queue

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        q = queue.Queue()
        q.put(root)
        deep = 0
        while q:
            deep +=1
            size = q.qsize()
            for i in range(size):
                node = q.get()
                if node.left == None and node.right == None:
                    return deep
                if node.left != None:
                    q.put(node.left)
                if node.right != None:
                    q.put(node.right)


tree1 = TreeNode(2,None,TreeNode(3,None,TreeNode(4,None,TreeNode(5,None,TreeNode(6)))))

print(Solution.minDepth(Solution,tree1))