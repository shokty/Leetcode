class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicty = {}
        for num in nums:
            if num not in dicty:
                dicty[num] = 0
            dicty[num] += 1
        sum = 0
        for element in dicty:
            if dicty[element] == 1:
                sum += element
        return sum