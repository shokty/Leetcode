class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        def find_subarrays(i):
            sety = set()
            counter = 0
            while i < len(A):
                sety.add(A[i])
                i += 1
                if len(sety) == K:
                    counter += 1
                    break
            while i < len(A):
                if A[i] in sety:
                    counter += 1
                    i += 1
                else:
                    break
            return counter
        sumy = 0
        for i in range(len(A)):
            sumy += find_subarrays(i)
        return sumy

print(Solution.subarraysWithKDistinct(Solution,A = [1,2,1,2,3], K = 2))
