class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        answear = []
        to_add = []
        dicty = {}
        for num in arr2:
            dicty[num] = 0
        for num in arr1:
            if num in dicty:
                dicty[num] += 1
            else:
                to_add.append(num)
        for num in arr2:
            answear += [num] * dicty[num]
        to_add.sort()
        return answear + to_add

print(Solution.relativeSortArray(Solution,[2,3,1,3,2,4,6,7,9,2,19],[2,1,4,3,9,6]))