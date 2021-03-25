class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if 1 not in nums:
            return True
        string = ''.join(str(x) for x in nums)
        string = string[string.index('1') + 1:]
        counter = 0
        for digit in string:
            if (digit == '1'):
                if counter < k:
                    return False
                counter = 0
            else:
                counter +=1
        return True
print(Solution.kLengthApart(Solution,
[1,0,0,1,0,1],2))