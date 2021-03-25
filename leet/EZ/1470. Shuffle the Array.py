class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        Xx = nums[:n]
        Yy = nums[n:]
        answear = []
        for i in range(n):
            answear.append(Xx[i])
            answear.append(Yy[i])
        return answear