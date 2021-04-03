# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodes_deep = {}
        def definedeaph(node):
            if node == None:
                return 0
            val = max(definedeaph(node.left),definedeaph(node.right)) + 1
            nodes_deep[node] = val
            return val
        definedeaph(root)
        def check_balance(node):
            if node == None:
                return True
            rightlen = leftlen = 0
            if node.right != None:
                rightlen = nodes_deep[node.right]
            if node.left != None:
                leftlen = nodes_deep[node.left]
            return abs(rightlen - leftlen) <=1 and \
                   check_balance(node.left) and check_balance(node.right)
        return check_balance(root)

tree2 = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4),TreeNode(4)),TreeNode(3)),TreeNode(2))
tree3 = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
tree = TreeNode(1,None,TreeNode(2,None,TreeNode(3)))
print(Solution.isBalanced(Solution,tree3))