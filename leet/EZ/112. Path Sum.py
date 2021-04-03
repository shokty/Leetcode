# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False;
        if root.left == None and root.right == None:
            if targetSum - root.val == 0:
                return True
            else:
                return False
        return self.hasPathSum(self,root.left,targetSum - root.val) or self.hasPathSum(self,root.right,targetSum - root.val)

tree = TreeNode(1,TreeNode(4),TreeNode(3))

print(Solution.hasPathSum(Solution,tree,3))