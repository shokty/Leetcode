class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        end = set()
        start = set()
        for path in paths:
            start.add(path[0])
            end.add(path[1])
        look = end.difference(start)
        return look.pop()
print(Solution.destCity(Solution,[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))