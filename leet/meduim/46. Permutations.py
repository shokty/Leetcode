class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answear = []
        def make_premute(curr,rest):
            if len(rest) == 0:
                answear.append(curr)
            for i in range(len(rest)):
                make_premute(curr + [rest[i]],rest[:i] + rest[i+1:])
        make_premute([],nums)
        return answear
print(Solution.permute(Solution,[1,1,2]))