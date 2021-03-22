class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicty = {}
        for i in range(len(nums)):
            num = nums[i]
            if (target-num) in dicty:
                return [num,target-num]
            dicty[num] = i
        return []