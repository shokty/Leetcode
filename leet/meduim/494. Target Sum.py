class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        len_of_numbs = len(nums)
        memo = {}
        def recusivesum(index,sum):
            if index == len_of_numbs and sum == S:
                return 1
            if index >= len_of_numbs:
                return 0

            string = str(index) + "," + str(sum)
            if string in memo:
                return memo[string]

            memo[string] = recusivesum(index+1,sum + nums[index]) + recusivesum(index+1,sum - nums[index])
            return memo[string]
        return recusivesum(0,0)

print(Solution.findTargetSumWays(Solution,[1, 1, 1, 1, 1],3))
