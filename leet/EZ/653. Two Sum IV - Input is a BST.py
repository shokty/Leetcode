# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        sety = set()
        def inorder(node):
            if node == None:
                return ;
            if (k - node.val) in sety:
                return True
            sety.add(node.val)
            return inorder(node.left) or inorder(node.right)
        return inorder(root)