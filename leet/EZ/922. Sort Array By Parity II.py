class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leny = len(nums)
        answear = [0] * leny
        odd_index = 1
        even_index = 0
        for num in nums:
            if num % 2 == 0:
                answear[even_index] = num
                even_index += 2
            else:
                answear[odd_index] = num
                odd_index += 2
        return answear