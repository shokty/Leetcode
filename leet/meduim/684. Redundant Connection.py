class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        dicty = {}
        stack  = []
        for edge in edges:
            start = edge[0]
            end = edge[1]
            if start not in dicty:
                dicty[start] = set([start])
            if end not in dicty:
                dicty[end] = set([end])
            if (end in dicty[start] or start in dicty[end]):
                stack.append(edge)
            else:
                dicty[start] = dicty[end] = dicty[start].union(dicty[end])
        if len(stack) == 0:
            return ;
        return stack.pop()

Input = [[3,4],[1,2],[2,4],[3,5],[2,5]]
print(Solution.findRedundantConnection(Solution,Input))