# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        memo = {1 : [TreeNode(0)]}
        def maketree(numnodes):
            ans = []
            if numnodes in memo:
                return memo[numnodes]
            for i in range(1, numnodes, 2):
                left_Trees = maketree(i)
                right_Trees = maketree(numnodes - i - 1)
                for left in left_Trees:
                    for right in right_Trees:
                        roottoadd = TreeNode(0)
                        roottoadd.left = left
                        roottoadd.right = right
                        ans.append(roottoadd)
            memo[numnodes] = ans
            return memo[numnodes]
        return maketree(N)


print(Solution.allPossibleFBT(Solution, 7))
