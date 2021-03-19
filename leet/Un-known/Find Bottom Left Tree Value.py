# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        Max = [0,root.val]
        def dfsbuttomleft(Node,deep):
            if Node == None:
                return None;
            if deep > Max[0]:
                Max[0] = deep
                Max[1] = Node.val
            dfsbuttomleft(Node.left,deep+1)
            dfsbuttomleft(Node.right,deep+1)

        dfsbuttomleft(root,0)
        return Max[1]


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution.findBottomLeftValue(Solution,root))

