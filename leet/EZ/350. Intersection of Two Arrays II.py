class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answear = []
        dicty = {}
        for k in nums1:
            if k in dicty:
                dicty[k] +=1
            else:
                dicty[k] = 1
        for num in nums2:
            if num in dicty and dicty[num] >= 1:
                answear.append(num)
                dicty[num] -=1
        return answear

print(Solution.intersect(Solution,
[1,2,2,1],
[2,2]))