class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        Max = 0
        spit = 0
        for i in range(len(arr)):
            Max = max(Max,arr[i])
            if Max == i:
                spit +=1
        return spit


arr = [1,0,2,3,4]
print(Solution.maxChunksToSorted(Solution,arr))