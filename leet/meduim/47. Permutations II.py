class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answear = []
        sety = set()
        def make_premute(curr,rest):
            if len(rest) == 0:
                curr_string = str(curr).strip('[]')
                if curr_string not in sety:
                    answear.append(curr)
                    sety.add(curr_string)
            for i in range(len(rest)):
                make_premute(curr + [rest[i]],rest[:i] + rest[i+1:])
        make_premute([],nums)
        return answear

print(Solution.permuteUnique(Solution,[1,1,2]));