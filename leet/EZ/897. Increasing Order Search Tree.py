# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import queue
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None;
        Q = queue.Queue()
        def bfs(node):
            if node == None:
                return ;
            else:
                bfs(node.left)
                Q.put(node.val)
                bfs(node.right)
        bfs(root)
        first = TreeNode(Q.get())
        temp = first
        while Q.qsize() > 0:
            temp.left = TreeNode(Q.get())
            temp = temp.right
        return first

tree = TreeNode(5,TreeNode(1),TreeNode(7))
Solution.increasingBST(Solution,tree)