class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        answear = []
        curr_min = 191478147
        for i in range(len(arr)-1):
            curr_min =  min(abs(arr[i]-arr[i+1]), curr_min)

        for i in range(len(arr) - 1):
            if abs(arr[i]-arr[i+1]) == curr_min:
                answear.append([arr[i],arr[i+1]])
        return answear