
class Solution(object):
    def removeDuplicates(self, nums):
        nodup = 0
        for i in range (1,len(nums)):
            if(nums[i] != nums[nodup]):
                nodup += 1
                nums[nodup] = nums[i]
        return nodup+1
        """
        :type nums: List[int]
        :rtype: int
        """

print(Solution.removeDuplicates(Solution,[1,1,2]))