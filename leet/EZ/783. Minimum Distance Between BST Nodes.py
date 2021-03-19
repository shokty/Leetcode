class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def find_min_dif(rot,mini):
            if rot != None:
                if rot.left != None:
                    left =  rot.val - rot.left.val
                    mini = min(left,mini)
                if rot.right != None:
                    right = rot.right.val - rot.val
                    mini = min(right,mini)
            return min(find_min_dif(rot.left),find_min_dif(rot.right),mini)
        return find_min_dif(root,1000)