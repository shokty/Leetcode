# Definition for a binary tree node.
import queue
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        answear = []
        dicty = {}
        def go_over_tree(node,deep):
            if node == None:
                return ;
            dicty.setdefault(deep, [0,0])
            dicty[deep][0] += node.val
            dicty[deep][1] += 1
            go_over_tree(node.left,deep+1)
            go_over_tree(node.right, deep + 1)
        go_over_tree(root,0)
        for i in range(len(dicty)):
            curr = dicty[i]
            answear.append(curr[0] / float(curr[1]))
        return answear


tree = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
print(Solution.averageOfLevels(Solution,tree))
