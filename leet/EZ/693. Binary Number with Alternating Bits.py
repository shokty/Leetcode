
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = str(bin(n))[2:]
        prev = binary[0]
        for i in range(1,len(binary)):
                if prev == binary[i]:
                    return False
                prev = binary[i]
        return True
print(Solution.hasAlternatingBits(Solution,7))