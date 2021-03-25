class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        mx = arr[len(arr) -1]
        arr[len(arr) -1] = -1
        for i in reversed(range(len(arr)-1)):
            tmx = max(mx, arr[i])
            arr[i] = mx
            mx = tmx
        return arr


print(Solution.replaceElements(Solution,[17,18,5,4,6,1]))