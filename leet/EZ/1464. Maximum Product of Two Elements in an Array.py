class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx1 = 0
        mx2 = 2
        for num in nums:
            if num > mx1:
                if mx1 > mx2:
                    mx2 = mx1
                mx1 = num
            elif num > mx2:
                mx2 = num
        return (mx2 -1)*(mx1 -1)

print(Solution.maxProduct(Solution,
[3,4,5,2]))