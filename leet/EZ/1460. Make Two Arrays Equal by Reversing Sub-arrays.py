import collections


class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        return collections.Counter(target) == collections.Counter(arr)

print(Solution.canBeEqual(Solution,[1,2,3,4],[2,4,1,3]))