class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) == 0:
            return 0
        lastseen = arr[0]
        counter = 0
        currmax = 0
        for location in arr:
            if location > lastseen:
                counter += 1
            else:
                currmax = max(currmax,counter)
                counter = 0
            lastseen = location
        return max(currmax,counter)