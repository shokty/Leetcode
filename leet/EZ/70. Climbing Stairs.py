class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {0 : 0 , 1 : 1 , 2 : 2}
        def ways_to_claim(n):
            if n in memo:
                return memo[n]
            memo[n] = ways_to_claim(n-1) + ways_to_claim(n-2)
            return memo[n]
        return ways_to_claim(n)

Solution.climbStairs()