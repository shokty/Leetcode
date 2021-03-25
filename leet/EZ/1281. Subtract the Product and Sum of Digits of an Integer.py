class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        add = 0
        mul = 1
        while n > 0:
            add += n%10
            mul *= n%10
            n /= 10
        return mul - add