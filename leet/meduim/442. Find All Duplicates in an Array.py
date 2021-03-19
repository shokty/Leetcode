class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answear = []
        for num in nums:
            if nums[abs(num)-1] > 0:
                nums[abs(num)-1] = nums[abs(num)-1]*-1
            else:
                answear.append(abs(num))
        return answear
print(Solution.findDuplicates(Solution,[4,3,2,7,8,2,3,1]))