class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        to_move = nums[-1]
        index = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < to_move:
                index = i
                break
        sordy =  sorted(nums[index:-1])
        return nums[0:index] + [to_move] + sordy

print(Solution.nextPermutation(Solution,
[1,2,3]))