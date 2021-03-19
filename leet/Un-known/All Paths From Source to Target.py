import queue


class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        S = set()
        n = len(graph)-1
        answear = []
        def bfs(currpath,vertex):
            currpath = currpath + [vertex]
            if (vertex == n):
                answear.append(currpath)
            for neighbor in graph[vertex]:
                    S.add(neighbor)
                    bfs(currpath, neighbor)
        bfs([],0)
        return answear

graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(Solution.allPathsSourceTarget(Solution,graph))