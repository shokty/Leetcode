class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        dicty = {}
        for i in range(lowLimit,highLimit +1):
            curr = sum(map(int, str(i)))
            if curr not in dicty:
                dicty[curr] = 0
            dicty[curr] += 1
        maxy = 0
        for balls in dicty.values():
            maxy = max(maxy,balls)
        return maxy

print(Solution.countBalls(Solution,1,10))