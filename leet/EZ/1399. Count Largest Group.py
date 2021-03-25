class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        if len(str(n)) == 1:
            return n
        k = str(n)[1:]
        return int(k) + 1
Solution.countLargestGroup(Solution,2)