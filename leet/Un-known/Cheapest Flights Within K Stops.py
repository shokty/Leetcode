import heapq

from urllib3.connectionpool import xrange


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = [[0 for i in xrange(n)] for j in xrange(n)]
        for edge in flights:
            graph[edge[0]][edge[1]] = edge[2]

        heap = [(0 , src, K +1)]
        while heap:
            costsofar,curvartex,disleft = heapq.heappop(heap)
            if(curvartex == dst):
                return costsofar
            if (disleft > 0):
                for vartex in range(n):
                    if graph[curvartex][vartex] != 0:
                        heapq.heappush(heap,((costsofar + graph[curvartex][vartex]),vartex,disleft-1))
        return -1


n = 3
edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(Solution.findCheapestPrice(Solution,n,edges,src,dst,k))