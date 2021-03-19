class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        Max = 0
        buy = prices[0]

        for i in range(len(prices)):
            Max = max(Max,prices[i]-buy)
            buy = min(buy,prices[i])
        return Max

prices = [7,1,5,3,6,4]
print(Solution.maxProfit(Solution,prices))
