# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        def guess(num):
            return 33 - num
        while (low <= high):
            mid = (int) (low + (high - low)/2)
            res = guess(mid)
            if (res == 0):
                return mid
            elif (res < 0) :
                high = mid-1
            else:
                low=mid+1
        return -1


print(Solution.guessNumber(Solution,100))