class Solution(object):
    def maxResult(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        memo = {}
        sum = 0
        i = 0
        while i < len(nums) - 1:
            sum += nums[i]
            max_i = -100000
            max_val = -100000
            for j in range(1,k):
                if i + j < len(nums):
                    if max_val < nums[i + j]:
                        max_i = i + j
                        max_val = nums[i + j]
            i += max_i
        return sum + nums[-1]


print(Solution.maxResult(Solution,
[10,-5,-2,4,0,3], 3))

