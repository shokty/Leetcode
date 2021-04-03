
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        answear = []
        def add_to_ans(node):
            if node == None:
                return ;
            for child in node.children:
                add_to_ans(child)
            answear.append(node.val)
        add_to_ans(root)
        return answear