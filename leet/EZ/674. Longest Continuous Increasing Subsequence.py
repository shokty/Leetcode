class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        curr = -1
        maximum = 1
        for num in nums:
            if num > curr:
                counter += 1
                curr = num
            else:
                maximum = max(maximum,counter)
                counter = 1
                curr = num
        return max(maximum,counter)

print(Solution.findLengthOfLCIS(Solution,
[2,1,3]))