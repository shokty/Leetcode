class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odds = []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odds.append(num)
        return even + odds