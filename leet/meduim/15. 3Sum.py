
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answear = []
        nums.sort()
        leny = len(nums)
        for i in range(leny):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l,r = i+1,leny-1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    answear.append([nums[i] , nums[l] , nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l +=1 #skiping on the same
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                    l += 1; r -=1
                elif s > 0:
                    r -=1
                else:
                    l +=1
        return answear
