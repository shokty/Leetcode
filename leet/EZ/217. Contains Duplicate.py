class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        S = set()
        for num in nums:
            if num in S:
                return True
            S.add(num)
        return False