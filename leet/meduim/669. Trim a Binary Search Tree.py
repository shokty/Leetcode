from typing import List, Any, Union


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dicty = {}
        for i in range(len(equations)):
            eq = equations[i]
            val = values[i]
            dicty[eq[0]] = [val,eq[1]]
            dicty[eq[1]] = [1/val,eq[0]]
        anwear: list[Union[Union[int, float], Any]] = []
        def dfs(sourse,target,sum):
            return 0

        for querie in queries:
            up = querie[0]
            down = querie[1]
            if up in dicty and down in dicty:
                anwear.append(dicty[up]/dfs(down,down,1))
            else:
                 anwear.append(-1)
        return anwear
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution.calcEquation(Solution,equations,values,queries))