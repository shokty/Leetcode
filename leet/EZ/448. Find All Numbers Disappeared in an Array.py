class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            num = abs(num) -1
            if nums[num] > 0:
                nums[num] = -nums[num]
        answear = []
        for i in range(len(nums)):
            if nums[i] > 0:
                answear.append(i+1)
        return answear

print(Solution.findDisappearedNumbers(Solution,[4,3,2,7,8,2,3,1]))