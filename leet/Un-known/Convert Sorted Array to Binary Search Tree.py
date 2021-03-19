# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def dfs(arr):
            if not arr:
                return None
            median = (len(arr)) // 2
            node = TreeNode(arr[median])
            node.left = dfs(arr[:median])
            node.right = dfs(arr[median+1:])
            return node

        root = dfs(nums)
        return root


print(Solution.sortedArrayToBST(Solution,[-10,-3,0,5,9]))
