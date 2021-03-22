class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        dicty = {}
        for i in range(N):
            dicty[i+1] = [False,0]
        for trasty in trust:
            dicty[trasty[0]][0] = True
            dicty[trasty[1]][1] += 1
        for i in range(N):
            if dicty[i+1] == [False,N-1]:
                return i+1
        return -1
N = 2
trust = [[1,2]]
print(Solution.findJudge(Solution,N,trust))