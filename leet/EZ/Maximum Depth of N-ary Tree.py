
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        Max = 0
        for child in root.children:
            Max = max(Max, self.maxDepth(self, child))

        return 1 + Max
