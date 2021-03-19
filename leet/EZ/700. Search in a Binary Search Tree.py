class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val == val:
                break
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return root

tree = TreeNode(4,TreeNode(2,TreeNode(1),TreeNode(3)),TreeNode(7))
tree2 = Solution.searchBST(Solution,tree,2)
print(tree)
print(tree2)