import functools
import operator


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        arry = []
        sum = start + 1;
        for i in range(n):
            arry.append(start + 2*i)
        return functools.reduce(operator.xor,arry)

print(Solution.xorOperation(Solution,1,7))