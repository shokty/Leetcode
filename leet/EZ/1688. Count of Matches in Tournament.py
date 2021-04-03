class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 1
        return (int) (n/2) + self.numberOfMatches(self,(int)(n/2) + n%2)

print(Solution.numberOfMatches(Solution,7))