class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sol1(self):
            hasy = {}
            for num in nums:
                if num not in hasy:
                    hasy[num] = 0
                hasy[num] += 1
            max_appernce = 0
            rnum = 0
            for number in hasy:
                if hasy[number] > max_appernce:
                    rnum = number
                    max_appernce = hasy[number]
            return rnum
        return sol1()