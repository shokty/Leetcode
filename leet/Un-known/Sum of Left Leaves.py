# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.sumofleftleaf(root.left,True)
        self.sumofleftleaf(root.right, False)
    def sumofleftleaf(self,root,amileft):
        if not root: return 0
        if(not root.left and not root.right ):
            if(amileft):
                return root.val
            return 0
        sum = 0
        if (root.left != None):
            sum = self.sumofleftleaf(root.left,True)
        if (root.right != None):
            sum +=self.sumofleftleaf(root.right,False)
        return sum
        """
        :type root: TreeNode
        :rtype: int
        """
