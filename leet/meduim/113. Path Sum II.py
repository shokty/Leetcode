# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        answear = []
        def pathSumWithflow(node,targetsum,flow):
            if node == None:
                return ;
            flow = flow + [node.val]
            targetsum -= node.val
            if node.left == None and node.right == None:
                if targetsum  == 0:
                    answear.append(flow)
            pathSumWithflow(node.right,targetsum,flow)
            pathSumWithflow(node.left, targetsum, flow)
        pathSumWithflow(root,targetSum,[])
        return answear

tree = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(-1)))
print(Solution.pathSum(Solution,tree,3))